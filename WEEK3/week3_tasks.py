# WEEK 3: FUNCTIONS & DICTIONARIES – HANDS-ON PRACTICE
# Developer's Arena Internship


# ✅ Task 1: Functions for Common Calculations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"

print("Task 1: Common Calculations")
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("-" * 50)

# ✅ Task 2: Currency Converter
def usd_to_inr(usd):
    return usd * 83.0

def inr_to_usd(inr):
    return inr / 83.0

print("Task 2: Currency Converter")
usd = float(input("Enter amount in USD: "))
print("In INR:", usd_to_inr(usd))
inr = float(input("Enter amount in INR: "))
print("In USD:", inr_to_usd(inr))
print("-" * 50)

# ✅ Task 3: Student Database using Dictionary
print("Task 3: Student Database")
students = {}

def add_student(name, grade):
    students[name] = grade

def display_students():
    for name, grade in students.items():
        print(f"{name}: {grade}")

add_student("Aparna", "A")
add_student("Dev", "B+")
display_students()
print("-" * 50)

# ✅ Task 4: Text Analyzer
print("Task 4: Text Analyzer")

def analyze_text(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    return num_words, num_chars

text = input("Enter text: ")
words, chars = analyze_text(text)
print(f"Words: {words}, Characters: {chars}")
print("-" * 50)

# ✅ Task 5: Simple Bank Account System
print("Task 5: Bank Account System")

account = {"balance": 0}

def deposit(amount):
    account["balance"] += amount
    print("Deposited:", amount)

def withdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient funds!")

def show_balance():
    print("Current Balance:", account["balance"])

deposit(1000)
withdraw(200)
show_balance()
print("-" * 50)

# ✅ Task 6: String Methods Practice
print("Task 6: String Methods")

message = "Welcome to Python Programming"
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Words:", message.split())
print("Length:", len(message))
print("-" * 50)
