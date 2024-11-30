def main():
    # Prompt user for two numbers
    print("Enter two numbers to calculate their sum, difference, product, quotient, and remainder.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform calculations
    sum_result = num1 + num2
    diff_result = num1 - num2
    product_result = num1 * num2
    int_quotient = int(num1 // num2) if num2 != 0 else "Undefined (division by zero)"
    remainder = num1 % num2 if num2 != 0 else "Undefined (division by zero)"
    frac_quotient = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

    # Display the results
    print("\nResults:")
    print(f"First Number: {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {product_result}")
    print(f"Integer Quotient: {int_quotient}")
    print(f"Remainder: {remainder}")
    print(f"Fractional Quotient: {frac_quotient}")

if __name__ == "__main__":
    main()
