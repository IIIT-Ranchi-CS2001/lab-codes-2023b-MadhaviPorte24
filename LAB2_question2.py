# Given string
S = "Ba Ba Black Sheep"

# 1. The length of the string
length_of_string = len(S)

# 2. The first occurrence of the letter 'e'
first_occurrence_e = S.find('e')

# 3. The total number of occurrences of 'a'
total_occurrences_a = S.count('a')

# 4. Generate "Ta Ta Black Sheep"
new_string = S.replace("Ba", "Ta", 2)  # Replaces the first two occurrences of "Ba" with "Ta"

# Print the results
print("Length of the string:", length_of_string)
print("First occurrence of 'e':", first_occurrence_e)
print("Total occurrences of 'a':", total_occurrences_a)
print("Modified string:", new_string)
