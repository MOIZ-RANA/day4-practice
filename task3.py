# Write a program that asks the user for a list index and prints the value. Handle the error if the index is out of range.
list=["aaple","banana","orange"]
print(list)
try: 
    user_input=int(input("Give Index: "))
    index=user_input
    value=list[index]
    print(index)
except TypeError:
    print("there is type issue")
except ValueError:
    print("there is value issue")
except IndexError:
    print("there is Index issue")