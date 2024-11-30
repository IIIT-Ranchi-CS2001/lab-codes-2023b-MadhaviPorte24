# Input: Get the list of integers from the user using list comprehension
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

# Mean: Calculate the mean of the list
mean = sum(numbers) / len(numbers)

# Median: Calculate the median of the list
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)

# For odd length, the median is the middle element, for even, it's the average of the two middle elements
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

# Mode: Calculate the mode of the list
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Find the maximum frequency to determine the mode
max_freq = max(frequency.values())
mode = [key for key, value in frequency.items() if value == max_freq]

# Output the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
