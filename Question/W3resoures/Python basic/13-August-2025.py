"""Write a Python program that will accept the base and height of a triangle and compute its area.
def HCF(a, b):
    while a != 0:
        a, b = (
            b,
            a % b,
        )  # ye hamre ishiliye use kiya he isme a ko hamne b manna he or b ko a%b ye ek loop isme hamesha a vli value b vale ke sath divide hogi and jab tak hogi jab tak and me koi common ya single value na aye
        return a
print(HCF(44, 6))
# ager isse hame lcm bhi likalni ho to hum
def LCM(a, b):
    return (a * b) // HCF(a, b)
print(LCM(44, 6))"""

"""Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
def check(a, b, c):
    if a == b or b == c or c == a:
        return 0
    else:
        return a + b + c


print(check(7, 7, 9))"""


"""Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
def check(a, b):
    sum = a + b
    if sum in range(15, 20):
        return 20
    else:
        return a + b
print(check(1, 5))"""


"""Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
def check(a, b):
    if a == b or abs(a + b) == 5 or abs(a - b) == 5:  #isme vo tin chize puchrha ek dono equal he kiya nhi or dono ka sum or sub 5 ke equal he to usse true returen krvado
        return "true"
print(check(3, 3))"""


"""Write a Python program to add two objects if both objects are integers.
def check(a, b):
    if not isinstance(a, int) or isinstance(b, int):
        return a + b
    else:
        return "error this is not and int"
print(check(2, 4.5))"""
"""Write a Python program that displays your name, age, and address on three different lines.d
name = input("e name")
age = input("e age")
ad = input("e ad")
print(f"your name:{name}\n your age:{age}\n your Adress is:{ad}")"""

"""Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49

def check(a, b):
    return (a + b) * (a + b)


print(check(2, 3))"""

"""Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
def check(a, i, y):
    return (a * i * y) // 100


print(check(10000, 3.5, 7))"""
# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
