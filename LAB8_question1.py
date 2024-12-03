import numpy as np

def calculate_group_counts():
    # Define the ticket prices as coefficients for the system of equations
    # Event 1: Roller Coaster
    roller_coaster_prices = [44, 38, 21]
    roller_coaster_total = 1412

    # Event 2: 4D Max Cinema
    cinema_prices = [32, 28, 15]
    cinema_total = 1024

    # Event 3: Cable Car
    cable_car_prices = [24, 20, 10]
    cable_car_total = 728

    # Represent the system of equations as Ax = B
    A = np.array([roller_coaster_prices, cinema_prices, cable_car_prices])
    B = np.array([roller_coaster_total, cinema_total, cable_car_total])

    # Solve for x (number of males, females, and kids)
    solution = np.linalg.solve(A, B)

    # Extract the solution
    males, females, kids = solution

    # Print results
    print(f"Number of males: {int(males)}")
    print(f"Number of females: {int(females)}")
    print(f"Number of kids: {int(kids)}")

if __name__ == "__main__":
    calculate_group_counts()
