import math

def calculate_triangle_properties():
    print("Enter the lengths of the three sides of the triangle:")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate perimeter
        perimeter = a + b + c

        # Calculate semi-perimeter
        s = perimeter / 2

        # Calculate area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Calculate angles using the cosine rule
        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle_C = 180 - angle_A - angle_B

        # Display the results
        print("\nTriangle Properties:")
        print(f"Sides: a = {a}, b = {b}, c = {c}")
        print(f"Perimeter: {perimeter}")
        print(f"Area: {area:.2f}")
        print(f"Angle A: {angle_A:.2f}°")
        print(f"Angle B: {angle_B:.2f}°")
        print(f"Angle C: {angle_C:.2f}°")
    else:
        print("\nThe entered sides do not form a valid triangle.")

if __name__ == "__main__":
    calculate_triangle_properties()
