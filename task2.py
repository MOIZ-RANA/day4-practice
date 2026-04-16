# Write a program that asks the user for a number and handles the error if the user enters a non-numeric value.
try:
    num=int(input("eneter number: "))
except ValueError:
    print(" write a number ")