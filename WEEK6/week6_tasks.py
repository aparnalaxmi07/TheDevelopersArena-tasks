# ---------------------------------------------------------
# WEEK 6: WORKING WITH EXTERNAL LIBRARIES – PRACTICE TASKS
# Developer's Arena Internship
# ---------------------------------------------------------

from datetime import datetime
import random
import requests

# Task 1: Display current date and time
print("Task 1: Current Date & Time")
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print("-" * 50)

# Task 2: Random data generator
print("Task 2: Random Data")
print("Random number:", random.randint(1, 100))
print("Random choice:", random.choice(["red", "blue", "green"]))
print("-" * 50)

# Task 3: JSON Data from API
print("Task 3: JSON Data from API")
url = "https://api.github.com/users/octocat"
data = requests.get(url).json()
print("User:", data["login"])
print("Followers:", data["followers"])
print("-" * 50)

# Task 4: Currency Converter using real rates
print("Task 4: Currency Converter")

api = "https://api.exchangerate-api.com/v4/latest/USD"
rates = requests.get(api).json()["rates"]

usd = float(input("Enter amount in USD: "))
inr = usd * rates["INR"]
print(f"{usd} USD = {inr:.2f} INR")
print("-" * 50)
