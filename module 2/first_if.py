#to check temperature
temperature = int(input("\nEnter temperature: "))

if temperature > 85:
    print("It's hot")
    print("Drink water")


#to check for age
age = int(input("\nEnter age: "))

if age >= 18:
    print("Adult")
    print("Can vote")

#to check budget
item_price = float(input("\nItem price: $"))
user_balance = float(input("Your balance : $"))

if user_balance >= item_price:
    print("Can afford")
    remaining_balance = user_balance - item_price
    print(f"You have: ${remaining_balance:.2f} left over!")


"""
if condition:
    # run if condition is true

# not indented
# always run

"""