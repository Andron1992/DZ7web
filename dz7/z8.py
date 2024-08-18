from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from Andrii import Subject, Grade


DATABASE_URL = "postgresql://andrii:2024@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def avg_grade_by_teacher(session, teacher_id):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject)\
        .filter(Subject.teacher_id == teacher_id)\
        .join(Grade)\
        .scalar()
