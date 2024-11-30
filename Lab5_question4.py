
input_string = input("Enter a string: ")

letter_count = {}

for char in input_string:
    
    if char.isalpha():
        char = char.lower()  
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

for letter, count in letter_count.items():
    print(f"{letter}: {count}")
