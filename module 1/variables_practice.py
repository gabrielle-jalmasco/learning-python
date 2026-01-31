# Variables as labeled boxes that hold information
product_name = "Wireless Headphones"
product_price = 79.99
quantity_in_stock = 150
is_on_sale = True

discount_percent = 20
sale_price = product_price * (1 - discount_percent / 100)

print("\n===== PRODUCT INFORMATION =====")
print("Product Name:", product_name)
print("Product Price:", product_price)
print("Quantity in Stock:", quantity_in_stock)
print("Is on Sale:", is_on_sale)
print("================================")

# Variables can CHANGE
print("\n=== UPDATING STOCK ===")
print("Original stock:", quantity_in_stock)

quantity_in_stock = quantity_in_stock - 10
print("After sale:", quantity_in_stock)

quantity_in_stock = quantity_in_stock + 50
print("After restock:", quantity_in_stock)
print("================================")

print("\n=== UPDATING PRICE ===")
print("Discount:", sale_price)
print("================================")
