"""Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated sequence.

Sample Data : 0100,0011,1010,1001,1100,1001Currency converter

Expected Output : 1010
def check():
    com = input("inter the number:").split(",")
    for x in com:
        dec = int(x, 2)
        if dec % 5 == 0:
            print(f" this is the num by 5 :{x}")
        else:
            print(f" this is the num not 5 :{x}")


check()"""

"""Write a Python program that accepts a string and calculates the number of digits and letters.

Sample Data : Python 3.2

Expected Output :

Letters 6
Digits 2

def check(i):
    dig = int()
    alp = int()
    space = int()
    for x in i:
        if x.isdigit():
            dig += 1
        elif x.isalpha():
            alp += 1
        else:
            space += 1
    return dig, alp, space
print(check("sd 2223fhvb awruk   fv123 "))"""
"""Write a Python program to check the validity of passwords input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters."""


def check(pas):
    if not 6 <= len(pas) <= 16:
        print("the lenght of pass should be 6 to 16")
        return
    special_chars = "@#$"
    has_lower = has_upper = has_digit = has_special = False

    for char in pas:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    if not has_lower:
        print("it not has lower")
    if not has_upper:
        print("it not has_upper")
    if not has_digit:
        print("it not has_digit")
    if not has_special:
        print("it not has_special")
    return " the password is valid"
