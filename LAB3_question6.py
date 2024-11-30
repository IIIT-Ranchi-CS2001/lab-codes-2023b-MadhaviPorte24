# Input: Get the string and the character to count from the user
string = input("Enter the string: ")
char_to_count = input("Enter the character to count: ")

# Initialize a counter for occurrences
count = 0

# Loop through each character in the string
for char in string:
    if char == char_to_count:
        count += 1

# Print the result
print(f"The character '{char_to_count}' occurs {count} time(s) in the string.")
