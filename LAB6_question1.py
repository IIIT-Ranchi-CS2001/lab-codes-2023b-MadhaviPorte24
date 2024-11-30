def my_zip(names, ids, points, strct=True):
    if strct:
        # If 'strct' is True, check that all lists are of equal length
        if len(names) == len(ids) == len(points):
            return list(zip(names, ids, points))
        else:
            raise ValueError("All lists must be of the same length when 'strct' is True")
    else:
        # If 'strct' is False, zip using the shortest list's length
        min_length = min(len(names), len(ids), len(points))
        return list(zip(names[:min_length], ids[:min_length], points[:min_length]))

# Example usage:
names = ['Alice', 'Bob', 'Charlie']
ids = [101, 102, 103, 104]
points = [200, 250, 300]

# When strct=True (strict zipping)
try:
    print(my_zip(names, ids, points, strct=True))  # Raises an error as lengths differ
except ValueError as e:
    print(e)

# When strct=False (zipping with minimum length)
print(my_zip(names, ids, points, strct=False))  # Output: [('Alice', 101, 200), ('Bob', 102, 250), ('Charlie', 103, 300)]
