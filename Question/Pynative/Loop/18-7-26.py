# Practice Problem: Write a program to print the first 10 natural numbers using a while loop. Each number should be printed on a new line.
i = 0
while i <10:
    i +=1
    print(i)
    
# Practice Problem: Write a program to display numbers from -10 to -1 using a for loop.
for i in range(-10,0):
    print(i)
    
# Practice Problem: Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.
for i in range(0,5):
    print(i)
else:
    print("done")
    
# Practice Problem: Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
def sum(m):
    result = 0
    for i in range(0,m+1): ## isme +1 ka use isiliye kiya he kyoki last element range me mention nhi hotahe to vo plus bhi nhi hoga to loop last number ke ek number age tak chalega tak vo last number bhi add ho sake 
        result +=i
    print(result)
sum(10)
    
# Practice Problem: Create a program that takes an integer and prints its multiplication table from 1 to 10.
def mul(m):
    for i in range(1,11):
        if i%m ==0:
         print(i)
mul(2)


# Practice Problem: Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1
def cu(n):
    m= 0
    for i in range(1,n+1):
        m = i*i*i
        print(m)
cu(9)

# ractice Problem: Given a list of numbers, iterate through it and print numbers that satisfy these conditions
# The number must be divisible by five.
# If the number is greater than 150, skip it and move to the next.
# If the number is greater than 500, stop the loop entirely.

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i >500:
        break
    if i >150:
        continue
    if i %5==0:
        print(i)    
    
