import hashlib
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from domain.models import User, Role, Program, Subject, SubjectOffering, Enrollment
from contracts.dtos import ProgramCreate, SubjectCreate, UserCreate, OfferingCreate, EnrollmentCreate

def _hash_password(plain: str) -> str:
    return hashlib.sha256(plain.encode('utf-8')).hexdigest()

class AdminService:
    def __init__(self, session: Session):
        self.s = session

    def add_user(self, dto: UserCreate) -> User:
        role = Role[dto.role.upper()]
        pwd_hash = _hash_password(dto.password)
        u = User(name=dto.name, username=dto.username, password_hash=pwd_hash, role=role)
        self.s.add(u); self.s.commit(); self.s.refresh(u)
        return u

    def add_program(self, dto: ProgramCreate) -> Program:
        p = Program(name=dto.name)
        self.s.add(p); self.s.commit(); self.s.refresh(p)
        return p

    def add_subject(self, dto: SubjectCreate) -> Subject:
        subj = Subject(program_id=dto.program_id, code=dto.code, title=dto.title)
        self.s.add(subj); self.s.commit(); self.s.refresh(subj)
        return subj

    def create_offering(self, dto: OfferingCreate) -> SubjectOffering:
        off = SubjectOffering(subject_id=dto.subject_id, teacher_id=dto.teacher_id, schedule=dto.schedule, room=dto.room)
        self.s.add(off); self.s.commit(); self.s.refresh(off)
        return off

    def enroll(self, dto: EnrollmentCreate) -> Enrollment:
        enr = Enrollment(student_id=dto.student_id, offering_id=dto.offering_id)
        self.s.add(enr); self.s.commit(); self.s.refresh(enr)
        return enr

    def report_subjects(self) -> List[Subject]:
        return list(self.s.scalars(select(Subject).order_by(Subject.id)))

    def report_enrollments(self) -> List[Enrollment]:
        return list(self.s.scalars(select(Enrollment).order_by(Enrollment.id)))

    def report_grades(self) -> List[Enrollment]:
        return list(self.s.scalars(select(Enrollment).where(Enrollment.grade != None).order_by(Enrollment.id)))

class TeacherService:
    def __init__(self, session: Session):
        self.s = session

    def view_schedule(self, teacher_id: int) -> List[SubjectOffering]:
        return list(self.s.scalars(select(SubjectOffering).where(SubjectOffering.teacher_id == teacher_id)))

    def assign_grade(self, enrollment_id: int, grade: int) -> Enrollment:
        e = self.s.get(Enrollment, enrollment_id)
        if not e:
            raise ValueError("Enrollment not found")
        e.grade = grade
        self.s.commit(); self.s.refresh(e)
        return e

class StudentService:
    def __init__(self, session: Session):
        self.s = session

    def view(self, student_id: int) -> dict:
        student = self.s.get(User, student_id)
        if not student or student.role != Role.STUDENT:
            raise ValueError("Student not found")
        enrollments = list(self.s.scalars(select(Enrollment).where(Enrollment.student_id == student_id)))
        return {"student": student, "enrollments": enrollments}

class AuthService:
    def __init__(self, session: Session):
        self.s = session

    def authenticate(self, username: str, password: str) -> Optional[User]:
        u = self.s.query(User).filter(User.username == username).one_or_none()
        if not u:
            return None
        if u.password_hash == _hash_password(password):
            return u
        return None
