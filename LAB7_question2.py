import random
import math
import matplotlib.pyplot as plt

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to separate primes and composites
def get_primes_and_composites(numbers):
    primes = []
    composites = []
    for num in numbers:
        if num > 1 and is_prime(num):
            primes.append(num)
        elif num > 1:
            composites.append(num)
    return primes, composites

# Main function
def main():
    # Input for K and N
    K = int(input("Enter the number of random numbers (minimum 10): "))
    N = int(input("Enter the upper limit for random numbers: "))

    if K < 10:
        print("K should be at least 10.")
        return

    # Generate a list of K random numbers within the range 1 to N
    random_numbers = [random.randint(1, N) for _ in range(K)]
    print(f"Generated list of random numbers: {random_numbers}")

    # Separate the list into primes and composites
    primes, composites = get_primes_and_composites(random_numbers)

    # Calculate squares of primes and square roots of composites
    prime_squares = [p**2 for p in primes]
    composite_roots = [math.sqrt(c) for c in composites]

    # Plotting the scatter plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Scatter plot for primes vs their squares
    axes[0].scatter(primes, prime_squares, color='blue', label='Prime Squares')
    axes[0].set_title('Prime Numbers vs Squares')
    axes[0].set_xlabel('Prime Numbers')
    axes[0].set_ylabel('Square of Prime Numbers')
    axes[0].legend()
    axes[0].grid(True)

    # Scatter plot for composites vs their square roots
    axes[1].scatter(composites, composite_roots, color='orange', label='Composite Square Roots')
    axes[1].set_title('Composite Numbers vs Square Roots')
    axes[1].set_xlabel('Composite Numbers')
    axes[1].set_ylabel('Square Root of Composite Numbers')
    axes[1].legend()
    axes[1].grid(True)

    # Adjust layout and display the plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
