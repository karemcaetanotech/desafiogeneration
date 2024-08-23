from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from models import db, Student
from schemas import student_schema, students_schema
from config import Config
from swagger_config import swagger_template, swagger_config
from flask_swagger import swagger

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(
        name=data['name'], age=data['age'],
        first_semester_grade=data['first_semester_grade'],
        second_semester_grade=data['second_semester_grade'],
        teacher_name=data['teacher_name'],
        classroom_number=data['classroom_number']
    )
    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return students_schema.jsonify(students)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    return student_schema.jsonify(student)

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    data = request.get_json()
    student.name = data['name']
    student.age = data['age']
    student.first_semester_grade = data['first_semester_grade']
    student.second_semester_grade = data['second_semester_grade']
    student.teacher_name = data['teacher_name']
    student.classroom_number = data['classroom_number']

    db.session.commit()
    return student_schema.jsonify(student)

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    db.session.delete(student)
    db.session.commit()
    return student_schema.jsonify(student)

# Swagger UI setup
SWAGGER_URL = '/swagger'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    '/apispec_1.json',
    config=swagger_config
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/apispec_1.json')
def apispec():
    return jsonify(swagger(app))

if __name__ == '__main__':
    app.run(debug=True)
