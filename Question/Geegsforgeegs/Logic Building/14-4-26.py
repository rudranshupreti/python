# Given an Integer n, find the reverse of its digits.
n = 2134
rev = 0
while n != 0:
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print(rev)
