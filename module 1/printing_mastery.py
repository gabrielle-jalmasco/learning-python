name = "Alex"
age = 25
balance = 1234.56789

# Simple Printing
print("\nHello World\n")

# Printing Variables

print(name)
print(age)

# Print multiple things
print("\nMy name is", name, "and I am", age, "years old.")

# String concatenation
print("Hello, " + name + "!")

# F-Srings
print(f"\nMy name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1} years old.")
print(f"In 10 years I will be {age + 10} years old.")

# F-strings can format numbers
print(f"\nMy balance is ${balance}") # shows all decimals
print(f"My balance is ${balance:.2f}") # .2f means 2 decimal places

# Special characters
print()
print("Line 1\n Line 2\n Line 3\n Line 4") # \n means new line
print("Column1\tColumn2\tColumn3") # \t means tab
print("She said \"Hello!\"") # \" means quote inside string

# TODO: Create a receipt using print 

item_input: str = str(input("Enter an item: "))
price_input: float = float(input("Enter price: $"))
quantity_input: int = int(input("Enter quantity: "))

subtotal_calculation: float = float(price_input * quantity_input)
tax_calculation = float(subtotal_calculation * 0.08)
total_calculation = float(subtotal_calculation + tax_calculation)


print("="*30)
print("COFFEE SHOP RECEIPT")
print("="*30)

print(f"Item: {item_input}")
print(f"Price: ${price_input}")
print(f"Quantity: {quantity_input}")
print("-"*30)
print(f"Subtotal: ${subtotal_calculation}")
print(f"Tax (8%): ${tax_calculation}")
print("-"*30)
print(f"TOTAL: ${total_calculation}")
print("="*30)
print("Thank you for your purchase!")
print("="*30)