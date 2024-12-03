# Given string
S1 = "Maha Bharat"

# 1. Convert the case: "mAHA bHARAT"
manipulated_case = S1.swapcase()

# 2. Extract "Bharat"
substring_bharat = S1.split()[1]

# 3. Generate "BharatBharatBharat"
repeated_bharat = substring_bharat * 3

# 4. Generate "Mera Bharat"
mera_bharat = "Mera " + substring_bharat

# 5. Generate "Mera Bharat Mahan"
mera_bharat_mahan = mera_bharat + " Mahan"

# Print the results
print("1. Case swapped string:", manipulated_case)
print("2. Extracted 'Bharat':", substring_bharat)
print("3. Repeated 'BharatBharatBharat':", repeated_bharat)
print("4. 'Mera Bharat':", mera_bharat)
print("5. 'Mera Bharat Mahan':", mera_bharat_mahan)
