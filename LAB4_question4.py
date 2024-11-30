# Create sets for singers and dancers using set comprehension
singers = {"John", "Alice", "Bob", "Eve", "Grace"}
dancers = {"Alice", "Bob", "Charlie", "Grace", "David"}

# Set operations to generate the required sets

# All artists of the class (union of singers and dancers)
all_artists = singers | dancers

# Allrounders of the class (intersection of singers and dancers)
allrounders = singers & dancers

# Dancers but not singers (dancers - singers)
dancers_not_singers = dancers - singers

# Singers but not dancers (singers - dancers)
singers_not_dancers = singers - dancers

# Dancers but not singers cum singers but not dancers (symmetric difference)
dancers_not_singers_cum_singers_not_dancers = singers ^ dancers

# Display the results
print(f"All artists of the class: {all_artists}")
print(f"Allrounders of the class: {allrounders}")
print(f"Dancers but not singers: {dancers_not_singers}")
print(f"Singers but not dancers: {singers_not_dancers}")
print(f"Dancers but not singers cum singers but not dancers: {dancers_not_singers_cum_singers_not_dancers}")
