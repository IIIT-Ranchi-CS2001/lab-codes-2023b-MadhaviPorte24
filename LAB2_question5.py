import math

# Input coefficients from the user
a = int(input("Enter the coefficient a (a ≠ 0): "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Determine the nature of the roots based on the discriminant
if d == 0:
    # One real repeated root
    R1 = R2 = -b / (2 * a)
    print(f"The equation has one real repeated root: R1 = R2 = {R1:.2f}")
elif d > 0:
    # Two distinct real roots
    R1 = (-b + math.sqrt(d)) / (2 * a)
    R2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"The equation has two distinct real roots:")
    print(f"R1 = {R1:.2f}")
    print(f"R2 = {R2:.2f}")
else:
    # Two complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-d) / (2 * a)
    print(f"The equation has two complex roots:")
    print(f"R1 = {real_part:.2f} + {imaginary_part:.2f}i")
    print(f"R2 = {real_part:.2f} - {imaginary_part:.2f}i")
