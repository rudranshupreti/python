"""Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 day

from datetime import date

f_date = date(2014, 3, 3)
l_date = date(2014, 3, 12)
delta = l_date - f_date
print(delta.days)"""

""" Write a Python program to get the volume of a sphere with radius six.
radius = int(input("Enter the radius:\n"))
volume = (4 / 3) * 3.24 * radius**3
print("the volume of sphere is:", volume)"""

"""Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
def deff_num(num):
    if num <= 17:
        return 17 - num
    else:
        return (num - 17) * 2

print(deff_num(10))
print(deff_num(36))"""


"""Write a Python program to test whether a number is within 100 of 1000 or 2000.
def number(number):
    return abs(100 - number) <= 100 or abs(2000 - number) <= 100
print(number(1000))
print(number(100))"""


"""Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
def check(num, num2, num3):
    sum = num + num2 + num3
    if num == num2 == num3:
        return sum * 3
    else:
        return sum
print(check(2, 2, 2))"""


"""Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
def check(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    else:
        return "Is" + str
print(check("Isok")) """


"""

Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
def check(str, num):
    return str * num
print(check("hello", 3))"""


"""Write a Python program to count the number 4 in a given list.
def check(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count
print(
    check(
        [
            1,
            2,
            3,
            4,
            4,
            4,
            5,
        ]
    )
)"""


"""Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
def check(str, num):
    if len(str) < 2:
        return str
    else:
        return str[:2] * num
print(check("yrtjyfthdc", 2))"""


"""Write a Python program to test whether a passed letter is a vowel or not.
def check(str):
    if str[0].lower() in ["a", "e", "i", "o", "u"]:
        return print("vowel")
    else:
        return print("not vowel")


print(check("lephent"))"""

""" Write a Python program that checks whether a specified value is contained within a group of values


def check(num):
    n = [1, 2, 3, 2, 3]
    for item in n:
        if item == num:
            return "true"
    else:
        return "False"


print(check(9))"""
