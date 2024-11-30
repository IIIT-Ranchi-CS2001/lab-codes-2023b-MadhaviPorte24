# Input: Get the sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize a counter for palindrome words
palindrome_count = 0

# Loop through each word in the list
for word in words:
    # Check if the word is a palindrome by comparing it to its reverse
    if word.lower() == word[::-1].lower():
        palindrome_count += 1

# Print the result
print(f"The number of palindrome words in the sentence is: {palindrome_count}")
