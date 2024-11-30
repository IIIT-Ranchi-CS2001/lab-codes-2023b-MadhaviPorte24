def calculate_parallel_impedance():
    print("Enter the impedances Z1 and Z2 in the form of real and imaginary parts:")
    
    # Input for Z1
    real1 = float(input("Enter the real part of Z1: "))
    imag1 = float(input("Enter the imaginary part of Z1: "))
    Z1 = complex(real1, imag1)
    
    # Input for Z2
    real2 = float(input("Enter the real part of Z2: "))
    imag2 = float(input("Enter the imaginary part of Z2: "))
    Z2 = complex(real2, imag2)
    
    # Calculate equivalent impedance for parallel connection
    if Z1 != 0 and Z2 != 0:
        Z_eq = 1 / ((1 / Z1) + (1 / Z2))
    else:
        Z_eq = 0 if Z1 == 0 and Z2 == 0 else Z1 if Z2 == 0 else Z2

    # Display results
    print("\nResults:")
    print(f"Z1: {Z1}")
    print(f"Z2: {Z2}")
    print(f"Equivalent Impedance (Z_eq): {Z_eq}")
    print(f"Real part of Z_eq: {Z_eq.real:.2f}")
    print(f"Imaginary part of Z_eq: {Z_eq.imag:.2f}")

if __name__ == "__main__":
    calculate_parallel_impedance()
