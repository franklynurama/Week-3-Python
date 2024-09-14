def divisible_by_ten(num):
    # Check if the number is divisible by 10 using the modulus operator
    if num % 10 == 0:
        return True
    else:
        return False

# Get user input for the number
num = int(input("Enter a number: "))

# Call the function and print the result
if divisible_by_ten(num):
    print(f"{num} is divisible by 10.")
else:
    print(f"{num} is not divisible by 10.")
