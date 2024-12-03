# Input: Get the value of n from the user
n = int(input("Enter the value of n: "))

# Header for the output
print("\nNumber\tSquare")
print("================")

# Initialize a counter
number = 1

# Loop to calculate and display squares
while number <= n:
    square = number ** 2
    print(f"{number}\t{square}")
    number += 1

