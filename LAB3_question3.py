# Input: Get the value of n from the user
n = int(input("Enter the number of terms (n): "))

# Initialize the first two terms of the Fibonacci series
a, b = 0, 1
count = 0

# Print the Fibonacci series
print("\nFibonacci Series:")
while count < n:
    print(a, end=" ")  # Print the current term
    # Update terms
    a, b = b, a + b
    count += 1
