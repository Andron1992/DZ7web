
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from Andrii import Student, Grade


DATABASE_URL = "postgresql://andrii:2024@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def top_student_by_subject(session, subject_id):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .first()
