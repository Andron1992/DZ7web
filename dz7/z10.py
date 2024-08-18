from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Andrii import Subject, Grade


DATABASE_URL = "postgresql://andrii:2024@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def courses_by_student_and_teacher(session, student_id, teacher_id):
    return session.query(Subject.name)\
        .join(Grade)\
        .join(Subject.teacher)\
        .filter(Grade.student_id == student_id)\
        .filter(Subject.teacher_id == teacher_id)\
        .all()