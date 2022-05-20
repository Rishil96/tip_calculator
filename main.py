# Project 2
# Tip Calculator

# greet user
print("Welcome to Tip Calculator.")

# get total bill
bill = float(input("What was the total bill?\n"))

# get number of people
people = float(input("How many people to split the bill?\n"))

# get tip percentage
tip = float(input("What percent tip would you like to give? 10, 12, or 15\n"))
tip = (tip + 100) / 100

# calculate amount per person
amount = round(bill * tip / people, 2)

# print final amount per person
print(f"Each person has to pay: ${amount}")
