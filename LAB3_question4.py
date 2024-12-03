# Input: Get the number and the limit from the user
number = int(input("Enter the number for the multiplication table: "))
limit = int(input("Enter the limit: "))

# Print the multiplication table
print(f"\nMultiplication Table of {number} up to {limit}:")
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")
