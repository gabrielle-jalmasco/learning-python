a = input("Enter number a: ")
a_convert = int(a)
b = input("Enter number b: ")
b_convert = int(b)

#basic
print(f"{a_convert} + {b_convert} = {a_convert + b_convert}")
print(f"{a_convert} - {b_convert} = {a_convert - b_convert}")
print(f"{a_convert} * {b_convert} = {a_convert * b_convert}")
print(f"{a_convert} / {b_convert} = {a_convert / b_convert}\n")

# special
print(f"{a_convert} // {b_convert} = {a_convert // b_convert}")
print(f"{a_convert} % {b_convert} = {a_convert % b_convert}")
print(f"{a_convert} ** {b_convert} = {a_convert ** b_convert}\n")

# practical use of // and %
total_minutes = 135

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes = {hours} hours and {minutes} minutes\n")

total_cents = 347

dollars = total_cents // 100
remaining = total_cents % 100
quarters = remaining % 25
remaining = remaining // 25
dimes = remaining // 10
remaining = remaining % 10
nickles = remaining // 5
pennies = remaining % 5

print(f"${total_cents/100:.2f} can be given as:")
print(f"  {dollars} dollars")
print(f"  {quarters} quarters")
print(f"  {dimes} dimes")
print(f"  {nickles} nickels")
print(f"  {pennies} pennies\n")

result1 = 2 + 3 * 4
result2 = (2 + 3) * 4

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

#compound interest calc
principal = float(input("Initial investment amount: $"))
rate = float(input("Annual interest raet: %"))
years = int(input("Number of years: "))

final_amount = principal * (1 + rate/100) ** years
profit = final_amount - principal

print(f"Intial Investment: %{principal:.2f}")
print(f"Interest Rate: {rate}%")
print(f"Time Period: {years} years")
print(f"Final Amount: ${final_amount:.2f}")
print(f"Total Profit: ${profit:,.2f}")