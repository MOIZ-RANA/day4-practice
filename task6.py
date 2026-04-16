# Write a program that asks the user for two numbers and divides them.

# Handle ZeroDivisionError and ValueError using except
# Use else to print the result only if no exception occurs
try:
    num1=int(input("eneter num1: "))
    num2=int(input("eneter num2: "))
    num3=num1/num2
except ZeroDivisionError:
    print("zero is not divisile by a number")
except ValueError:
    print("try a number, as it is not divisile by a number")
else: 
    print(num3)