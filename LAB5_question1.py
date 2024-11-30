import math
point1 = (4,5,6)
point2 = (3,5,4)

def euclidean_distance(p1, p2):

    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

distance = euclidean_distance(point1, point2)

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Euclidean Distance: {distance:.2f}")
