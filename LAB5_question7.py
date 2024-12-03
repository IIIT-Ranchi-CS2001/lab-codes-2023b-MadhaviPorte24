# Input: Get customer details using list comprehension
customer_names = [input(f"Enter customer name {i+1}: ") for i in range(3)]
customer_ids = [input(f"Enter customer ID {i+1}: ") for i in range(3)]
shopping_points = [int(input(f"Enter shopping points for customer {i+1}: ")) for i in range(3)]

# Construct a list of tuples using zip()
customer_data_zip = list(zip(customer_names, customer_ids, shopping_points))

# Construct a list of tuples manually without using zip()
customer_data_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(3)]

# Display the results
print("\nCustomer data using zip():")
print(customer_data_zip)

print("\nCustomer data without using zip():")
print(customer_data_manual)
