1: Install Python (If Not Installed Yet)

 python.org.

2: Create a Python Virtual Environment

Open CMD

Navigate to your folder/project directory

cd path/to/your/project/folder

Create a virtual environment by running:

python -m venv venv

Activate the virtual environment:

Windows:

venv\Scripts\activate

3: Install Flask

pip install Flask

4: Create Your Flask Application File (app.py)

Open your text editor (VS Code) and create a file named app.py in your project folder.

from flask import Flask, jsonify, request

app = Flask(__name__)

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

5: Run Your Flask Application

python app.py

6: Test the API Using Postman

1.6: Open Postman

If you haven't installed Postman, download it here: https://www.postman.com/downloads/

After installation, open Postman.

2.6: Test the API with Postman

Get All Students (GET request)

Open Postman.

Create a new request

Ser the method to GET from the dropdown menu

http://127.0.0.1:5000/students

Click Send

Result

[
    {
        "age": 22,
        "email": "juan@gmail.com",
        "id": 1,
        "name": "Juan Carlos",
        "section": "BSIT-4B"
    },
    {
        "age": 21,
        "email": "jose@gmail.com",
        "id": 2,
        "name": "Jose Rizal",
        "section": "BSIT-2A"
    },
    {
        "age": 20,
        "email": "juan@gmail.com",
        "id": 3,
        "name": "Juan Luna",
        "section": "BSIT-3A"
    },
    {
        "age": 20,
        "email": "andres@gmail.com",
        "id": 4,
        "name": "Andres Bonifacio",
        "section": "BSIT-3A"
    },
    {
        "age": 21,
        "email": "justin@gmail.com",
        "id": 5,
        "name": "Justin Bieber",
        "section": "BSIT-2A"
    }
]

Get a Student by ID (GET request)

In Postman, set the method to GET 

http://127.0.0.1:5000/students/1

You can replace 1 with the any student ID you want to retrieve

Result

{
    "age": 22,
    "email": "juan@gmail.com",
    "id": 1,
    "name": "Juan Carlos",
    "section": "BSIT-4B"
}

Add a New Student (POST request)

set the method to POST

http://127.0.0.1:5000/students

Go to Body
Select raw radio button
Add new student you want to add

Then enter the student data in JSON format like this:

{
    "name": "New Student",
    "section": "BSIT-1A",
    "email": "newstudent@gmail.com",
    "age": 20
}

Click Send

Result

{
    "age": 20,
    "email": "newstudent@gmail.com",
    "id": 6,
    "name": "New Student",
    "section": "BSIT-1A"
}

Update a Student (PUT request)

set the method to PUT

http://127.0.0.1:5000/students/1

You can replace 1 with the student ID you want to update

Go to Body
Select raw radio button

Enter the data you want to update

{
  "name": "Updated Student"
}

Click Send

Result

{
    "age": 22,
    "email": "juan@gmail.com",
    "id": 1,
    "name": "Updated Student",
    "section": "BSIT-4B"
}

Delete a student (DELETE request)

set the method to DELETE.

http://127.0.0.1:5000/students/1

You can change the 1 with any student ID you want to delete

Click Send

Result

{
  "message": "Student deleted"
}

