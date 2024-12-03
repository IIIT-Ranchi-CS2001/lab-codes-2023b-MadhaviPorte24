import numpy as np

def main():
    # User inputs for shapes of the 3D arrays
    shape1 = tuple(map(int, input("Enter the shape of the first 3D array (e.g., 3 4 2): ").split()))
    shape2 = tuple(map(int, input("Enter the shape of the second 3D array (e.g., 2 3 3): ").split()))

    # Generate random arrays
    A1 = np.random.randint(1, 100, size=shape1)  # Elements between 1 and 99
    A2 = np.random.randint(1, 100, size=shape2)

    print(f"\nArray A1:\n{A1}")
    print(f"\nArray A2:\n{A2}")

    # Select elements divisible by 5 from A1
    divisible_by_5 = A1[A1 % 5 == 0]
    print(f"\nElements of A1 divisible by 5:\n{divisible_by_5}")

    # Select elements divisible by 4 from A2
    divisible_by_4 = A2[A2 % 4 == 0]
    print(f"\nElements of A2 divisible by 4:\n{divisible_by_4}")

    # Join both arrays to form a single dimensional array
    combined_array = np.concatenate((divisible_by_5, divisible_by_4))
    print(f"\nCombined 1D array:\n{combined_array}")

    # Determine the largest possible square matrix size
    n = int(np.sqrt(len(combined_array)))
    square_matrix_size = n * n

    # Construct the square matrix
    square_matrix = combined_array[:square_matrix_size].reshape(n, n)
    print(f"\nLargest possible square matrix:\n{square_matrix}")

if __name__ == "__main__":
    main()
