def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price  # Calculate the discount amount
        final_price = price - discount_amount  # Calculate the final price
        return final_price
    else:
        return price  # Return the original price if discount is less than 20%

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price != original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")
