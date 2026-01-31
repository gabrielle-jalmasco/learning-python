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

#ask for monthly budget
monthly_budget_input = input("Enter your monthly budget: $")
monthly_budget_input_convert = float(monthly_budget_input)
print(monthly_budget_input_convert)


#five expenses for the month
expense_1 = input("Enter your expenses (1): $", )
expense_1_convert = float(expense_1)
print(expense_1_convert)

expense_2 = input("Enter your expenses (2): $")
expense_2_convert = float(expense_2)
print(f"First expense: {expense_2_convert}\n")

expense_3 = input("Enter your expenses (3): $")
expense_3_convert = float(expense_3)
print(expense_3_convert)

expense_4 = input("Enter your expenses (4): $")
expense_4_convert = float(expense_4)
print(expense_4_convert)

expense_5 = input("Enter your expenses (5): $")
expense_5_convert = float(expense_5)
print(expense_5_convert)

#calculation
total_budget_for_the_month = monthly_budget_input_convert
print(f"Total budget for the month: {total_budget_for_the_month}")


total_spent = expense_1_convert + expense_2_convert + expense_3_convert + expense_4_convert + expense_5_convert
print(f"Total expense for the month: {total_spent}")