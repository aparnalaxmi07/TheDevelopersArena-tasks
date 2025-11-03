# WEEK 2: CONTROL FLOW & DATA STRUCTURES – HANDS-ON PRACTICE
# Developer's Arena Internship
# ✅ Task 1: Number Guessing Game
import random

print("Task 1: Number Guessing Game")
secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("🎉 Correct! You guessed it!")
elif guess > secret:
    print("Too high! Try again.")
else:
    print("Too low! Try again.")

print("-" * 50)

# ✅ Task 2: Age Categorizer
print("Task 2: Age Categorizer")
age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child.")
elif age < 20:
    print("You are a Teenager.")
else:
    print("You are an Adult.")

print("-" * 50)

# ✅ Task 3: Shopping List Manager
print("Task 3: Shopping List Manager")

shopping_list = []

while True:
    print("\nCurrent List:", shopping_list)
    print("Options: add / remove / quit")
    action = input("What do you want to do? ").lower()

    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found!")
    elif action == "quit":
        break
    else:
        print("Invalid choice!")

print("Final Shopping List:", shopping_list)
print("-" * 50)

# ✅ Task 4: Multiplication Table Generator
print("Task 4: Multiplication Table Generator")

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("-" * 50)

# ✅ Task 5: Simple Login System
print("Task 5: Simple Login System")

username = "admin"
password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful! ✅")
else:
    print("Login Failed ❌")

print("-" * 50)

# ✅ Task 6: Practice List Operations
print("Task 6: List Operations")

numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)
numbers.append(6)
numbers.remove(3)
numbers.sort()
print("Modified List:", numbers)

print("Task 6 completed!")
print("-" * 50)
