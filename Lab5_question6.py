# Function to sort employees based on salary in descending order
def sort_employees_by_salary(employees):
    # Using a simple selection sort algorithm
    employee_list = list(employees.items())
    
    for i in range(len(employee_list)):
        max_index = i
        for j in range(i + 1, len(employee_list)):
            if employee_list[j][1] > employee_list[max_index][1]:
                max_index = j
        
        employee_list[i], employee_list[max_index] = employee_list[max_index], employee_list[i]
    
    return employee_list

employees = {}
for i in range(5):
    name = input(f"Enter the name of employee {i+1}: ")
    salary = float(input(f"Enter the salary of {name}: "))
    employees[name] = salary

sorted_employees = sort_employees_by_salary(employees)

print("\nEmployee Ranking based on Salary (Highest Salary First):")
for rank, (name, salary) in enumerate(sorted_employees, 1):
    print(f"Rank {rank}: {name} - Salary: {salary}")
