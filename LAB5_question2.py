
names = [f"Student_{i+1}" for i in range(10)] 
roll_nos = [i+1 for i in range(10)] 
marks = [70 + i*2 for i in range(10)] 

students_details = list(zip(names, roll_nos, marks))

sorted_students = sorted(students_details, key=lambda x: x[2])

for student in sorted_students:
    print(student)
