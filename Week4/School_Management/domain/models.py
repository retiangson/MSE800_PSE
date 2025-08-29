from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from infrastructure.db import Base
import enum

class Role(enum.Enum):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[Role] = mapped_column(Enum(Role), nullable=False)

    teachings: Mapped[list["SubjectOffering"]] = relationship(back_populates="teacher")
    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="student")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name!r}, username={self.username!r}, role={self.role.name})"

class Program(Base):
    __tablename__ = "programs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    subjects: Mapped[list["Subject"]] = relationship(back_populates="program", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Program(id={self.id}, name={self.name!r})"

class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    program_id: Mapped[int] = mapped_column(ForeignKey("programs.id"), nullable=False)

    program: Mapped[Program] = relationship(back_populates="subjects")
    offerings: Mapped[list["SubjectOffering"]] = relationship(back_populates="subject", cascade="all, delete-orphan")

    __table_args__ = (UniqueConstraint("program_id", "code", name="uq_subject_per_program"),)

    def __repr__(self):
        return f"Subject(id={self.id}, code={self.code!r}, title={self.title!r})"

class SubjectOffering(Base):
    __tablename__ = "subject_offerings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    schedule: Mapped[str] = mapped_column(String, nullable=False)
    room: Mapped[str] = mapped_column(String, nullable=True)

    subject: Mapped[Subject] = relationship(back_populates="offerings")
    teacher: Mapped["User"] = relationship(back_populates="teachings")
    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="offering", cascade="all, delete-orphan")

    def __repr__(self):
        subj_code = self.subject.code if self.subject else None
        return f"Offering(id={self.id}, subject={subj_code}, teacher_id={self.teacher_id}, schedule={self.schedule!r})"

class Enrollment(Base):
    __tablename__ = "enrollments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    offering_id: Mapped[int] = mapped_column(ForeignKey("subject_offerings.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    grade: Mapped[int | None] = mapped_column(Integer, nullable=True)

    student: Mapped["User"] = relationship(back_populates="enrollments")
    offering: Mapped[SubjectOffering] = relationship(back_populates="enrollments")

    __table_args__ = (UniqueConstraint("student_id", "offering_id", name="uq_enrollment_once"),)

    def __repr__(self):
        return f"Enrollment(id={self.id}, student_id={self.student_id}, offering_id={self.offering_id}, grade={self.grade})"
