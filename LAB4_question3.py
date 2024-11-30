# Input: Create the list of course codes and course names
course_codes = ["CS1001", "CS1002", "CS1003", "CS1004"]
course_names = ["Python", "Data Structures", "Algorithms", "Database Systems"]

# Create a new list by combining course code and course name
course_list = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]

# Output the new list
print(course_list)
