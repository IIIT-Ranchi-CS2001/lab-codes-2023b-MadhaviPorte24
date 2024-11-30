def my_max(*args):
    # Check if any arguments were passed
    if not args:
        raise ValueError("my_max() expects at least one argument")
    
    # Initialize the first element as the maximum
    max_value = args[0]
    
    # Iterate through the rest of the elements to find the maximum
    for value in args[1:]:
        if value > max_value:
            max_value = value
    
    return max_value

# Example usage:

# For a list of integers
list_data = [1, 5, 8, 3, 7]
print("Max in list:", my_max(*list_data))  # Output: 8

# For a set of integers
set_data = {12, 45, 78, 23, 56}
print("Max in set:", my_max(*set_data))  # Output: 78

# For a tuple of integers
tuple_data = (10, 20, 15, 30, 25)
print("Max in tuple:", my_max(*tuple_data))  # Output: 30
