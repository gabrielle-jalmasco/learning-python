#even odd check
number = int(input("\nEnter number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#age category
age = int(input("\nEnter age: "))

if age >= 18:
    print("You are adult.")
else:
    print("You are minor.")


#pass or fail
score = int(input("\nEnter test score (0-50): "))
percent_passage = (score / 50) * 100

if score >= 38:
    print("Pass.")
    print(f"Your score is: {percent_passage}%")
else:
    print("Failed.")
    print(f"Your score is: {percent_passage}%")
    print("You need at least 75% to pass.")