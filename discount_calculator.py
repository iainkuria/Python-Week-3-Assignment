def calculate_discount(price, discount_percent):
    """Calculate final price after discount if discount is 20% or more"""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Get user input
item_price = float(input("Enter the item's original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(item_price, discount)

# Display result
if discount >= 20:
    print(f"Final price after {discount}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Price remains: ${item_price:.2f}")