from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from Andrii import Student, Grade


DATABASE_URL = "postgresql://andrii:2024@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def top_5_students_by_avg_grade(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .limit(5)\
        .all()
