# Input: Get the string from the user
string = input("Enter a string: ")

# Flag to check if all characters are alphanumeric
all_alphanumeric = True

# Check each character in the string
for char in string:
    if not char.isalnum():  # Check if the character is not alphanumeric
        all_alphanumeric = False
        break  # Exit the loop as soon as a non-alphanumeric character is found

# Print the result
print(all_alphanumeric)
