# Taking input from the user
input_string = input("Enter a comma-separated string: ")

# Splitting the string by comma and removing any extra spaces
input_list = input_string.split(',')

# Using map and filter with lambda to find all letters, convert them to uppercase
letters_upper = list(map(lambda x: ''.join(filter(str.isalpha, x)).upper(), input_list))
letters_upper = list(filter(lambda x: x != '', letters_upper))  # Filtering out empty strings
print("Letters converted to uppercase:", letters_upper)

# Using map and filter with lambda to find all digits, then square them
digits_squared = list(map(lambda x: int(x)**2, filter(lambda x: x.isdigit(), input_string)))
print("Squares of the digits:", digits_squared)
