def my_sort(data, key):
    # Implementing a basic bubble sort algorithm to avoid using sorted()
    n = len(data)
    
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare based on the key
            if data[j][key] > data[j+1][key]:
                # Swap the elements if they are in the wrong order
                data[j], data[j+1] = data[j+1], data[j]
                
    return data

# Example usage:
data = [
    ('Alice', 101, 200),
    ('Bob', 102, 250),
    ('Charlie', 103, 300)
]

# Sorting based on customer name (key = 0)
print("Sorted by customer name:", my_sort(data.copy(), 0))

# Sorting based on customer ID (key = 1)
print("Sorted by customer ID:", my_sort(data.copy(), 1))

# Sorting based on shopping points (key = 2)
print("Sorted by shopping points:", my_sort(data.copy(), 2))
