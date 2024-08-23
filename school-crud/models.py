from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    first_semester_grade = db.Column(db.Float, nullable=False)
    second_semester_grade = db.Column(db.Float, nullable=False)
    teacher_name = db.Column(db.String(100), nullable=False)
    classroom_number = db.Column(db.Integer, nullable=False)
