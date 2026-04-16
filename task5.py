# Write a program that asks the user for a number and converts it to an integer.

# Use try to handle invalid input
# Use else to print the number if no error occurs

try: 
    num=int(input("Write aa number: "))
except ValueError:
    print("you type invalid input")
else: 
    print(num)
