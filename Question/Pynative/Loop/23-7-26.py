# Exercise Purpose: This logic-heavy exercise combines Type Conversion, Mathematical Iteration, and Power Operations. It tests your ability to break a complex problem into steps: isolate digits, raise them to a power, and compare the sum.
def am(k):
    n  = str(k)
    l=""
    o=0
    for  i in n:
        i = int(i)
        l=i*i*i
        o+=l 
    if k==o:
        print("yes")
    else:
        print("no")
am(153)



# Practice Problem: Write a program to print a right-angled triangle pattern where each row contains increasing numbers up to the row number

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")
    
# Practice Problem: Print a 5*5 square of stars where the middle is empty, leaving only the border.
n=5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
        else:
                print(" ", end=" ")
    print() 
