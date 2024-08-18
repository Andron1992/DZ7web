from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from Andrii import Group, Student, Grade


DATABASE_URL = "postgresql://andrii:2024@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def avg_grade_by_group(session, subject_id):
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Student)\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Group.id)\
        .all()
