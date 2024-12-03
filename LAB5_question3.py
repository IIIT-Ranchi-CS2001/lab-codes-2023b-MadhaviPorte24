
names = [f"Student_{i+1}" for i in range(10)] 
roll_nos = [i+1 for i in range(10)]  
marks = [70 + i*2 for i in range(10)]  

students_details = []
for i in range(len(names)):
    students_details.append((names[i], roll_nos[i], marks[i]))


for i in range(len(students_details)):
    for j in range(i + 1, len(students_details)):
        if students_details[i][2] > students_details[j][2]:
            students_details[i], students_details[j] = students_details[j], students_details[i]


for student in students_details:
    print(student)
