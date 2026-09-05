# Given a positive integer n, find the sum of the first n natural numbers.
def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum(9))

# Given a positive integer n, we have to find the sum of squares of first n natural numbers.


def square(m):
    multi = 0
    for i in range(1, m + 1):
        multi += i**2
    return multi


print(square(2))
