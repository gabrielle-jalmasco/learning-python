user_age = int(input("Enter age: "))

print(f"Age: {user_age}")
print(f"Are you a teenager (13-19)? Age >= 13: {user_age >= 13}")
print(f"Are you a adult (18+)? Age >= 18: {user_age >= 18}")
print(f"Are you a senior (65+)? Age >= 65: {user_age >= 65}")
print(f"Are you exactly 25? Age == 25: {user_age == 25}\n")

item_price = float(input("Enter price: $"))
budget = float(input("Enter budget: $"))

print(f"\nCan you afford it? {item_price <= budget}")
print(f"Is it over budget? {item_price > budget}")
print(f"Is it exactly your budget? {item_price == budget}")
print(f"Do you have money left? {budget > item_price}\n")

correct_password = "Python123"
user_password = input("Enter password: ")

print(f"\nPassword correct? {user_password == correct_password}")
print(f"Password incorrect? {user_password != correct_password}")

# string  comparisons == are case-sensitive