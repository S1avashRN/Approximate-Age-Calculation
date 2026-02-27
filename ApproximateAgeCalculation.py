from datetime import datetime

print("Welcome.\n\n")

Name = input("Please enter your first name: ")

Check = 0
while Check < 1 | Check > 2:
    Check = int(input("Enter one of these codes below:\n1. Solar year (Iran).\n2. AD/CE (Georgian calendar).\nEnter: "))
    if Check < 1 | Check > 2:
        print("Error.\nYou can only choose between 1 and 2.\n")

print("\n\nProgram is over.")