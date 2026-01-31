# expense tracker v1.0 by gab

import datetime
from datetime import date

print("="*50)
print("WELCOME TO EXPENSE TRACKER 1.0 BY GAB")
print("="*50)

name_input = input("\nYour Name: ")

date_greeting = print(f"\nWelcome, {name_input}!")
date_info = date.today()
print(f"It is now: {date_info}\n")

monthly_budget_input = input("Enter your monthly budget: $")
monthly_budget_input_convert = float(monthly_budget_input)
print(monthly_budget_input_convert)

expense_1 = input("Enter your monthly budget: $")
expense_1_convert = float(expense_1)
print(expense_1_convert)

