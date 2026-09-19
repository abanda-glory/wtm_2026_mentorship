# Total number of student entries
count = int(input("How many student entries do you want to create?\n"))

# An empty dictionary to store student information
student_records = {}

for entry in range(1, count+1):
    print(f"{'-'*3}Entry {entry}{'-'*3}")
    name = input("Enter student's name\n")
    score = float(input("Enter student's score\n"))

    # Add the name and score to student record
    student_records[name] = score

# Loop student records to evalaute scores and grade
print(f"{'='*20}\n STUDENT EVALUATION\n {'='*20}")

passed = 0
failed = 0


for name, score in student_records.items():
    if score < 0 or score > 100:
        grade = '-'
        status = "Invalid Score"
    elif score >= 70:
        grade = "A"
        status = "Passed with Distinction"
    elif score >= 50:
        grade = "B"
        status = "Passed"
    else:
        grade = "F"
        status  = "Needs Improvement"

    # Count number passed and number failed
    if score < 50:
        failed += 1
    else:
        passed += 1

    print(f"-Name: {name} | Score: {score} | Grade: {grade} | Status: {status}")




print(f"{'='*20}\n CLASS PERFORMANCE\n {'='*20}")

total_scores = 0

if count > 0:
    average_score = sum(student_records.values()) / count

    print(f"Average Score: {average_score:.2f}\nTotal Passed: {passed}\nTotal Failed: {failed}")
else:
    print("No student records entered")