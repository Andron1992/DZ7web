import random
from datetime import date

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Імпорт моделей
from Andrii import Student, Group, Teacher, Subject, Grade, Base


DATABASE_URL = "postgresql://andrii:2024@localhost:5432/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()


groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()


teachers = [Teacher(fullname=faker.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()


subjects = [Subject(name=faker.word(), teacher=random.choice(teachers)) for _ in range(5)]
session.add_all(subjects)
session.commit()


for _ in range(30):
    student = Student(fullname=faker.name(), group=random.choice(groups))
    session.add(student)
    session.commit()

    for subject in subjects:
        grades = [Grade(student=student, subject=subject, grade=random.uniform(60, 100), date_received=date.today()) for _ in range(5)]
        session.add_all(grades)
        session.commit()
