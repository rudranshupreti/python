# Practice Problem: Write a function called demo() that accepts two parameters: a name and an age. The function should print these values directly to the console.
def f(a,b):
    print (a,b)
f("rudra",3)

# Practice Problem: Write a recursive function addition() that calculates the sum of numbers from 0 to 10. A recursive function is a function that calls itself to solve smaller instances of the same problem

def add (num):
    if num ==0:
        return num
    return num + add(num-1)
print(add(10))