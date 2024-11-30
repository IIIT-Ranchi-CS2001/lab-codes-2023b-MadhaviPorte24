# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Remove spaces and convert to lowercase for uniformity
processed_string = user_input.replace(" ", "").lower()

# Check if the string is a palindrome
if processed_string == processed_string[::-1]:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
