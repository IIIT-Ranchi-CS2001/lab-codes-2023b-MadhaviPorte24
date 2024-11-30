# Input: Get the number from the user
number = int(input("Enter a number: "))

# Initialize variables
original_number = number
digit_sum = 0

# Loop to calculate the sum of digits
while number > 0:
    digit = number % 10  # Get the last digit
    digit_sum += digit   # Add it to the sum
    number //= 10        # Remove the last digit

# Display the result
print(f"The sum of the digits of {original_number} is {digit_sum}.")
