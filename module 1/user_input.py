print("=== Welcome to the Greeting Program ===\n")

name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you!")

city = input("What city do you live in? ")
print(f"Oh cool, {city} sounds like a nice place!\n")

# input() always return a string!

print("=== Age Calculator ===\n")
birth_year_str = input("What year were you born? ")
print(f"You entered: {birth_year_str}")
print(f"Type of birth_year_str: {type(birth_year_str)}")

birth_year = int(birth_year_str)
print(f"Type of birth_year: {type(birth_year)}")

current_year = 2026
age = current_year - birth_year
print(f"You are approximately {age} years old!")

print("\n=== Height Converter ===\n")

height_inches = float(input("Enter your height in inches: "))
height_cm = height_inches * 2.54
print(f"Your height in centimeters is: {height_cm} cm")