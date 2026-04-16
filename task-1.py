# Write a program that divides two numbers and handles both:

# division by zero
# invalid input
try: 
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))
    num3=num1/num2
    print("Result"+ num3)
except ValueError:
    print("there is issue")
except ZeroDivisionError:
    print("There is issue2")