# Practice Problem: Write a program to use a loop to find the factorial of a given number (e.g., 5!). The factorial of N is the product of all integers from 1 to N.
def  l (f):
    d=1
    for i in range(1,f+1):
        d = i*d
        print(d)
l(5)

# ractice Problem: The Collatz conjecture states that if you start with any positive integer n, and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process. The sequence will always eventually reach 1. Write a program to print this sequence for a given number.
i=5
while i !=1:
    if i%2==0:
        i=i//2
    else:
        i= i*3+1
    print(i)
    
# Practice Problem: Write a program to check if a number is an Armstrong number. An Armstrong number (for a 3-digit number) is an integer such that the sum of the cubes of its digits is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).
i=153
while i !=0:
    s=i//10
    j=s*s*s
    print(j)