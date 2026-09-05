"""Write a Python program to print the following string in a specific format.
Twinkle, twinkle, little star,
        How I wonder what you are!
                Up above the world so high,
                Like a diamond in the sky.
Twinkle, twinkle, little star,
        How I wonder what you are!

print(
    "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\tHow I wonder what you are"
)"""

# Write a Python program to find out what version of Python you are using.
"""import sys
print("version is")
print(sys.version)
"""
"""# Write a Python program to display the current date and time.
import datetime

print(datetime.datetime.now())"""

"""# Write a Python program that calculates the area of a circle based on the radius entered by the user.
radius = 1.3
area = 3.14 * radius * radius
print("area of circle is :", area)"""

"""# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
first_name = input("entre you first name\n")
last_name = input("enter your last name\n")
reverse = last_name + first_name
print("your reverse name is:", reverse)"""

"""Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
number = input("enter the numbers:")
print(number.split(","))
print(tuple(number.split(",")))"""

"""Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
filename = input("enter the filename:")
print(filename.split(".")[-1])"""

"""Write a Python program to display the first and last colors from the following list.
color_list = ["Red", "Green", "White", "Black"]
print("first color is:", color_list[0])
print("last color is:", color_list[-1])"""

"""Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
exam_st_date = (11, 12, 2014)
print(
    "the exam will start from :",
    exam_st_date[0],
    "/",
    exam_st_date[1],
    "/",
    exam_st_date[2],
)
"""
"""Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
n = input("enter a number:")
n1 = int(n)
n2 = n1 * n1
n3 = n1 * n1 * n1
result = n1 + n2 + n3
print("the result number is:", result)"""

"""Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument
print(len.__doc__)"""
