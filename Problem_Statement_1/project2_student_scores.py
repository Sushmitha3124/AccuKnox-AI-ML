import matplotlib.pyplot as plt
import statistics

# Sample student data from a mock API response
students = [
    {"name": "Anu", "score": 78},
    {"name": "Ravi", "score": 85},
    {"name": "Meena", "score": 92},
    {"name": "Kiran", "score": 67},
    {"name": "Priya", "score": 88}
]

# Extract student names and scores
names = [student["name"] for student in students]
scores = [student["score"] for student in students]

# Calculate average score
average_score = statistics.mean(scores)

print("Student Scores:")

for student in students:
    print(student["name"], ":", student["score"])

print("Average Score:", round(average_score, 2))

# Create a bar chart
plt.bar(names, scores)
plt.xlabel("Student Name")
plt.ylabel("Test Score")
plt.title("Student Test Scores")
plt.ylim(0, 100)

plt.show()