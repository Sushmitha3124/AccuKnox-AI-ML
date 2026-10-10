from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"name": "Anu", "score": 78},
    {"name": "Ravi", "score": 85},
    {"name": "Meena", "score": 92},
    {"name": "Kiran", "score": 67},
    {"name": "Priya", "score": 88}
]

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=False, port=5000)