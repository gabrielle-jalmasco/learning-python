# type casting (conversion)

#string to integer
age_string = "25"
age_number = int(age_string)#convert string to number/integer
print(f"String '25' + 5 would cause error")
print(f"Integer 25 + 5 = ({age_number+5})")

#string to float
price_string = "25"
price_number = float(price_string)
print(f"Price with tax: ${price_number * 1.08:.2f}")

# number to string
score = 100
score_text = str(score)
print("Your score is: " + score_text + " points!")

# float to integer (drops decimal, doesn't round off)
temperature = 98.6
temperature_int = int(temperature)
print(f"Float: {temperature}. Integer: {temperature_int}")

#int to float
whole_number = 42
decimal_number = float(whole_number)
print(f"Integer: {whole_number}. Float: {decimal_number}")

# Bill Splitter

print("\n")
print("="*30)
total_bill = float(input("Enter the total bill amount: $"))
number_of_people = int(input("How many people are splitting it? "))
tip_percent = float(input("Tip percentage: "))

tip_amount = total_bill * (tip_percent/100)
total_with_tip = total_bill + tip_amount
per_person = total_with_tip / number_of_people

print(f"Bill: ${total_with_tip:.2f}")
print(f"Tip: ({tip_percent}%): ${tip_amount})")
print(f"Total: ${total_with_tip:.2f}")
print(f"Each person pays: ${per_person:.2f}")