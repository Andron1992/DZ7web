from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Andrii import Student


DATABASE_URL = "postgresql://andrii:2024@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def students_by_group(session, group_id):
    return session.query(Student.fullname)\
        .filter(Student.group_id == group_id)\
        .all()
