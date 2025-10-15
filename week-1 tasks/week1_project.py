# WEEK 1 PROJECT: PERSONAL INFORMATION MANAGER

# Collect user information
print("===== Personal Information Manager =====")

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
hobbies = input("Enter your hobbies (comma separated): ")

# Process the hobbies into a list
hobby_list = hobbies.split(",")

# Display the collected information neatly
print("\n----- Your Personal Information -----")
print(f"Name     : {name}")
print(f"Age      : {age}")
print(f"City     : {city}")
print("Hobbies  :")

for h in hobby_list:
    print(" -", h.strip())

print("--------------------------------------")
print("Thank you for using the Personal Information Manager!")
print("--------------------------------------")
