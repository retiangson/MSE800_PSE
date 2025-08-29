import getpass
from tabulate import tabulate
from infrastructure.db import get_engine, get_session_factory, Base
from infrastructure.config import DEFAULT_ADMIN, DB_URL
from business.services import AdminService, TeacherService, StudentService, AuthService
from contracts.dtos import ProgramCreate, SubjectCreate, UserCreate, OfferingCreate, EnrollmentCreate
from domain.models import Role, User, Program, Subject, SubjectOffering, Enrollment
from sqlalchemy.exc import IntegrityError

def initialize_db_and_admin():
    engine = get_engine(DB_URL)
    Base.metadata.create_all(engine)
    session = get_session_factory(engine)()
    # ensure default admin exists
    admin_cfg = DEFAULT_ADMIN
    existing = session.query(User).filter(User.username == admin_cfg.get('username')).one_or_none()
    if not existing:
        svc = AdminService(session)
        try:
            svc.add_user(UserCreate(name=admin_cfg.get('name'), username=admin_cfg.get('username'), password=admin_cfg.get('password'), role='ADMIN'))
            print(f"Default admin '{admin_cfg.get('username')}' created.")
        except IntegrityError:
            session.rollback()
    session.close()

def prompt_login(session):
    auth = AuthService(session)
    print("=== School Management System ===")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    user = auth.authenticate(username, password)
    if not user:
        print("Login failed. Check credentials.")
    return user

def admin_menu(session, user):
    svc = AdminService(session)
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add User") 
        print("2. Add Program")
        print("3. Add Subject")
        print("4. Create Offering")
        print("5. Enroll Student")
        print("6. Reports")
        print("7. Logout")
        choice = input("Select: ").strip()
        try:
            if choice == '1':
                name = input("Enter name: ").strip()
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                role = input("Enter role [ADMIN/TEACHER/STUDENT]: ").strip().upper()
                u = svc.add_user(UserCreate(name=name, username=username, password=password, role=role))
                print("Created:", u)
            elif choice == '2':
                name = input("Program name: ").strip()
                p = svc.add_program(ProgramCreate(name=name))
                print("Created:", p)
            elif choice == '3':
                program_id = int(input("Program ID: ").strip())
                code = input("Subject code: ").strip()
                title = input("Title: ").strip()
                s = svc.add_subject(SubjectCreate(program_id=program_id, code=code, title=title))
                print("Created:", s)
            elif choice == '4':
                subject_id = int(input("Subject ID: ").strip())
                teacher_id = int(input("Teacher User ID: ").strip())
                schedule = input("Schedule (e.g., Mon 09:00-11:00): ").strip()
                room = input("Room (optional): ").strip() or None
                off = svc.create_offering(OfferingCreate(subject_id=subject_id, teacher_id=teacher_id, schedule=schedule, room=room))
                print("Created:", off)
            elif choice == '5':
                student_id = int(input("Student User ID: ").strip())
                offering_id = int(input("Offering ID: ").strip())
                enr = svc.enroll(EnrollmentCreate(student_id=student_id, offering_id=offering_id))
                print("Enrolled:", enr)
            elif choice == '6':
                print("Reports:\n1. Subjects\n2. Enrollments\n3. Grades\n4. Back")
                rc = input("Select: ").strip()
                if rc == '1':
                    rows = svc.report_subjects()
                    table = [(s.id, s.program.name, s.code, s.title) for s in rows]
                    print(tabulate(table, headers=["ID","Program","Code","Title"]))
                elif rc == '2':
                    rows = svc.report_enrollments()
                    table = [(e.id, e.student.name, e.offering.subject.code, e.offering.schedule) for e in rows]
                    print(tabulate(table, headers=["EnrollID","Student","Subject","Schedule"]))
                elif rc == '3':
                    rows = svc.report_grades()
                    table = [(e.id, e.student.name, e.offering.subject.code, e.grade) for e in rows]
                    print(tabulate(table, headers=["EnrollID","Student","Subject","Grade"]))
            elif choice == '7':
                break
            else:
                print("Invalid choice.")
        except Exception as ex:
            print("Error:", ex)

def teacher_menu(session, user):
    svc = TeacherService(session)
    while True:
        print("\n--- Teacher Menu ---")
        print("1. View Schedule") 
        print("2. Assign Grade")
        print("3. Logout")
        choice = input("Select: ").strip()
        try:
            if choice == '1':
                rows = svc.view_schedule(user.id)
                table = [(o.id, o.subject.code, o.subject.title, o.schedule, o.room) for o in rows]
                print(tabulate(table, headers=["OfferingID","Code","Title","Schedule","Room"]))
            elif choice == '2':
                enrollment_id = int(input("Enrollment ID: ").strip())
                grade = int(input("Grade (0-100): ").strip())
                e = svc.assign_grade(enrollment_id, grade)
                print("Updated:", e)
            elif choice == '3':
                break
            else:
                print("Invalid choice.")
        except Exception as ex:
            print("Error:", ex)

def student_menu(session, user):
    svc = StudentService(session)
    while True:
        print("\n--- Student Menu ---")
        print("1. View Schedule & Grades") 
        print("2. Logout")
        choice = input("Select: ").strip()
        try:
            if choice == '1':
                data = svc.view(user.id)
                student = data['student']
                enrolls = data['enrollments']
                print(f"Student: {student.name} (id={student.id})")
                table = [(e.id, e.offering.subject.code, e.offering.subject.title, e.offering.schedule, e.grade) for e in enrolls]
                print(tabulate(table, headers=["EnrollID","Code","Title","Schedule","Grade"]))
            elif choice == '2':
                break
            else:
                print("Invalid choice.")
        except Exception as ex:
            print("Error:", ex)

def run():
    initialize_db_and_admin()
    engine = get_engine(DB_URL)
    session_factory = get_session_factory(engine)
    while True:
        session = session_factory()
        user = prompt_login(session)
        if not user:
            session.close()
            cont = input("Try again? (y/n): ").strip().lower()
            if cont != 'y':
                print("Goodbye."); break
            continue
        print(f"Login successful ({user.role.name})") 
        if user.role == Role.ADMIN:
            admin_menu(session, user)
        elif user.role == Role.TEACHER:
            teacher_menu(session, user)
        elif user.role == Role.STUDENT:
            student_menu(session, user)
        session.close()
        again = input("Do you want to login as another user? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye."); break
