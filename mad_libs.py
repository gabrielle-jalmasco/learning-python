print("=== Welcome to Mad Libs! ===")
print("Answer the following questions:\n")

adjective1 = input("Enter an adjective (describing word): ")
noun1 = input("Enter a noun (person, place, or thing): ")
verb1 = input("Enter a verb (action word): ")
adverb1 = input("Enter an adverb (modifier): ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")

print("\n" + "="*50)
print("YOUR STORY: ")
print("="*50 + "\n")

print(f"Once upon a time, there was a {adjective1} {noun1}.")
print(f"One day, {noun1} decided to {verb1} {adverb1} to go to the park.")
print(f"And decided to {verb2} some {adjective2} {noun2}.")
print("\n" + "="*50)

print("\nThanks for playing!")
print("="*50)