"""Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

Sample Output :

fizzbuzz
1
2
fizz
4
buzz

for x in range(1, 50):
    if x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    elif (x % 3, 5) == 0:
        print("fizzbuzz")
    else:
        print(x)
"""

"""Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# Create 2D array using nested list comprehension
result = [[i * j for j in range(n)] for i in range(m)]

# Print the result
print("Generated 2D Array:", result)"""

"""Write a Python program that accepts a string and calculates the number of digits and letters.

Sample Data : Python 3.2

Expected Output :

Letters 6
Digits 2
def check(l):"""
