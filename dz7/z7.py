from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Andrii import Student, Group, Grade


DATABASE_URL = "postgresql://andrii:2024@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def grades_by_group_and_subject(session, group_id, subject_id):
    return session.query(Student.fullname, Grade.grade)\
        .join(Group)\
        .filter(Student.group_id == group_id)\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .all()
