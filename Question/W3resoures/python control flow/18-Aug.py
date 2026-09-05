"""Write a Python program that accepts a word from the user and reverses it.
def change():
    wd = input("enter the name :")
    rev = ""
    for x in wd:
        rev = x + rev
    print(rev)
change()"""

"""Write a Python program to count the number of even and odd numbers in a series of numbers

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :

Number of even numbers : 5
Number of odd numbers : 4


def check():
    even = []
    odd = []
    num = list(input("enter your number:"))
    for x in num:
        digit = int(x)
        if digit % 2 == 0:
            even.append(digit)
        else:
            odd.append(digit)
    return even, odd
print(check())  # <-- return ko print kiya"""

"""Write a Python program that prints each item and its corresponding type from the following list.

Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]"""

"""Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

Note : Use 'continue' statement.

Expected Output : 0 1 2 4 5

for i in range(0, 6):
    if i % 3 == 0:
        print("")
    else:
        print(i)"""
"""Write a Python program to get the Fibonacci series between 0 and 50.

a, b = 0, 1
while a <= 50:
    print(a, end=",")
    a, b = b, a + b"""
