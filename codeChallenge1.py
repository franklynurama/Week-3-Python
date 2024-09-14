def large_power(base, exponent):
    # Calculate the power of base raised to exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Get user input for base and exponent
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Call the function with user input and print the result
if large_power(base, exponent):
    print(f"The result of {base} to the power of {exponent} is greater than 5000.")
else:
    print(f"The result of {base} to the power of {exponent} is not greater than 5000.")
