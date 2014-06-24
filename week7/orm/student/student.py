from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

from sqlalchemy import func

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.name, self.age)

#Use it when you are in console
    def __repr__(self):
        return self.__str__()


class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    value = Column(Float)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", backref="grades")


engine = create_engine("sqlite:///university.db")
Base.metadata.create_all(engine)

session = Session(bind=engine, autocommit=True)
print("Add new person into table")

session.add_all([Student(name="ladald", age=21), Student(name="dadas", age=18),
                Student(name='assd', age=21), Student(name='sfg', age=30)])

all_students = session.query(Student).all()
print(all_students)

lqlq = session.query(Student).filter(Student.name == "dadas").one()
print(lqlq)

lqlq.grades = [Grade(value=5), Grade(value=6), Grade(value=4), Grade(value=3)]

lqlq_avg_grades = session.query(func.avg(Grade.value)).filter(Student.id == lqlq.id).one()
print(lqlq_avg_grades)

thirty_years = session.query(Student).filter(Student.age == 30).all()
print(thirty_years)
