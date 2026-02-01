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
print(f"\nTotal budget for the month: {total_budget_for_the_month}")

# total spent
total_spent = expense_1_convert + expense_2_convert + expense_3_convert + expense_4_convert + expense_5_convert
print(f"\nTotal expense for the month: {total_spent}")

# remaining budget
remaining_budget = total_budget_for_the_month - total_spent
print(f"\nRemaining budget: ${remaining_budget:.2f}")

# percentage of budget used
percentage_budget_used = total_spent / total_budget_for_the_month * 100
print(f"\nPercentage of the budget used: %{percentage_budget_used:.2f}")

# average expense amount
average_expense_amount = expense_1_convert + expense_2_convert + expense_3_convert + expense_4_convert + expense_5_convert / total_budget_for_the_month
print(f"Average expense amount: ${average_expense_amount}")