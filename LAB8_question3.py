import numpy as np

def Create_Array(*args):
    # Get the number of arguments passed, which determines the size of the square matrix
    n = len(args)
    
    # Create an n x n matrix filled with zeros
    array = np.zeros((n, n), dtype=int)
    
    # Place the elements in the diagonal
    np.fill_diagonal(array, args)
    
    return array

# Test the function with an example
result = Create_Array(1, 2, 3, 4)
print("Generated Array:")
print(result)
