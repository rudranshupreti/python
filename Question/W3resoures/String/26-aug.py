"""Write a Python program to remove the nth index character from a nonempty string.


def check(n, str):
    s = list(str)
    for i in range(len(s)):
        if i == n:
            s.pop(n)
    print(s)

check(2, "jytwerfgwrxdcgcx")"""

"""Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.


def check(s1, s2):
    final = s1[0] + s2 + s1[-1]
    print(final)
check("hello", "bye")"""

"""Write a Python program to remove characters that have odd index values in a given string


def check(s):
    num = list(s)
    final = []
    for i in range(len(num)):
        if i % 2 != 0:
            final.append(num[i])
    print("".join(final))
check("jhgvjhv")"""
