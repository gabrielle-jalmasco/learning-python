# These are shortcuts for common operations

score = 100

# Instead of: score = score + 10
score += 10
print(f"After += 10: {score}")  # 110

# Instead of: score = score - 25
score -= 25
print(f"After -= 25: {score}")  # 85

# Instead of: score = score * 2
score *= 2
print(f"After *= 2: {score}")   # 170

# Instead of: score = score / 2
score /= 2
print(f"After /= 2: {score}")   # 85.0

# Practical example: Shopping cart
print("\n=== SHOPPING CART ===")
cart_total = 0

# Add items
item1_price = 29.99
cart_total += item1_price
print(f"Added item ($29.99). Cart total: ${cart_total:.2f}")

item2_price = 15.50
cart_total += item2_price
print(f"Added item ($15.50). Cart total: ${cart_total:.2f}")

item3_price = 42.00
cart_total += item3_price
print(f"Added item ($42.00). Cart total: ${cart_total:.2f}")

# Apply 10% discount
cart_total *= 0.90
print(f"After 10% discount: ${cart_total:.2f}")