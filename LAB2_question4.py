# Input details from the user
name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")
marks = int(input("Enter marks secured in Mathematics (out of 100): "))

# Determine grade point and remark based on marks
if 90 <= marks <= 100:
    grade_point = 10
    remark = "Outstanding"
elif 80 <= marks <= 89:
    grade_point = 9
    remark = "Excellent"
elif 70 <= marks <= 79:
    grade_point = 8
    remark = "Very Good"
elif 60 <= marks <= 69:
    grade_point = 7
    remark = "Good"
elif 50 <= marks <= 59:
    grade_point = 6
    remark = "Average"
elif 35 <= marks <= 49:
    grade_point = 5
    remark = "Pass"
else:
    grade_point = 0
    remark = "Fail"

# Display student details
print("\nStudent Details")
print("Name:        ", name)
print("Roll Number: ", roll_number)
print("Marks:       ", marks)
print("Grade Point: ", grade_point)
print("Remark:      ", remark)
