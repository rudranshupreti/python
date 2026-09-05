# In a normal 6-faced dice, 1 is opposite to 6, 2 is opposite to 5, and 3 is opposite to 4. Hence a normal if-else-if block can be placed
def dei(n):
    return 7 - n


print(dei(4))

# Given a number n, find the sum of its digits.

# Examples :

# Input: n = 687
# Output: 21
# Explanation: The sum of its digits are: 6 + 8 + 7 = 21


def Allsum(n):
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum


print(Allsum(12345))
