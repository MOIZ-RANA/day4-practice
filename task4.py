# Write a function count_vowels(text) that counts and returns the number of vowels in a given string.

def count_vowels(text):
    count=0
    vowels="aeiouAEIOU"
    for char in vowels:
        if char in vowels:
            count+=1
    return count

my_str="Data Engineering is good"
result=count_vowels(my_str)
print(result)