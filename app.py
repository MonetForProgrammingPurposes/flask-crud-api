from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Student API! Try accessing /students to see the list of students."



students = [
    {"name": "Juan Carlos", "section": "BSIT-4B", "id": 1, "email": "juan@gmail.com", "age": 22},
    {"name": "Jose Rizal", "section": "BSIT-2A", "id": 2, "email": "jose@gmail.com", "age": 21},
    {"name": "Juan Luna", "section": "BSIT-3A", "id": 3, "email": "juan@gmail.com", "age": 20},
    {"name": "Andres Bonifacio", "section": "BSIT-3A", "id": 4, "email": "andres@gmail.com", "age": 20},
    {"name": "Justin Bieber", "section": "BSIT-2A", "id": 5, "email": "justin@gmail.com", "age": 21}
]



@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)



@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((student for student in students if student["id"] == student_id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"message": "Student not found"}), 404



@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    new_student['id'] = max(student['id'] for student in students) + 1  
    students.append(new_student)
    return jsonify(new_student), 201



@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((student for student in students if student["id"] == student_id), None)
    if student:
        data = request.get_json()
        student.update(data)
        return jsonify(student)
    else:
        return jsonify({"message": "Student not found"}), 404



@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = next((student for student in students if student["id"] == student_id), None)
    if student:
        students.remove(student)
        return jsonify({"message": "Student deleted"})
    else:
        return jsonify({"message": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
