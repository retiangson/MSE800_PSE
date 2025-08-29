from dataclasses import dataclass
from typing import Optional

@dataclass
class ProgramCreate:
    name: str

@dataclass
class SubjectCreate:
    program_id: int
    code: str
    title: str

@dataclass
class UserCreate:
    name: str
    username: str
    password: str
    role: str  # 'ADMIN' | 'TEACHER' | 'STUDENT'

@dataclass
class OfferingCreate:
    subject_id: int
    teacher_id: int
    schedule: str
    room: Optional[str] = None

@dataclass
class EnrollmentCreate:
    student_id: int
    offering_id: int
