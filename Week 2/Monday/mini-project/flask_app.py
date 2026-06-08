from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {
        "id" : 1,
        "name" : "Alice",
        "course" : "Computer Science"
    },
    {
        "id" : 2,
        "name" : "Bob",
        "course" : "Data Science"
    },
    {
        "id" : 3,
        "name" : "Christian",
        "course" : "Criminal Justice"
    },
    {
        "id" : 4,
        "name" : "Samantha",
        "course" : "Data Science"
    },
    {
        "id" : 5,
        "name" : "Billy",
        "course" : "Nursing"
    }
]

@app.get("/students")
def get_students():
    return jsonify(students)

@app.get("/students/<id>")
def get_student_from_id(id):
    id = int(id)
    return jsonify(list(filter(lambda x : x["id"] == id, students)))
        
@app.post("/students")
def add_student():
    data = request.json
    students.append({
        "id" : students[-1]["id"] + 1,
        "name" : data["name"],
        "course" : data["course"]
    })
    return jsonify(students), 201

@app.put("/students/<id>")
def put_student_from_id(id):
    try:
        data = request.json
        student = get_student_from_id(id)[0]
        student["name"] = data["name"]
        student["course"] = data["course"]
        return jsonify(students), 200
    except IndexError:
        return f"ID '{id}' does not exist.", 400

@app.delete("/students/<id>")
def delete_student_from_id(id):
    try:
        student = get_student_from_id(id)[0]
        students.remove(student)
        return f"Student '{student["name"]}' with id '{student["id"]}' was removed.", 200
    except IndexError:
        return f"ID '{id}' does not exist.", 400

if __name__ == "__main__":
    app.run(debug=True)
