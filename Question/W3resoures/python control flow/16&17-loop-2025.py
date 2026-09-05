"""Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
li = []
for x in range(1500, 2700):
    if (x % 7 == 0) and (x % 5 == 0):
        li.append(str(x))
print(",".join(li))"""

"""Write a Python program to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
import random


def rand(user):
    user = int(input("enter the number:"))
    rand = random.randint(1, 3)
    if rand == user:
        return "you won"
    else:
        return f"you lose the number is {rand}"


print(rand(2))"""
"""Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
n = 5
for i in range(n):
    for j in range(i):
        print("*", end="")
    print("")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")
