# Practice Problem: Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function twice: once using positional arguments and once using keyword arguments.
def g ( w,v):
    print(v)
    print (w,v)
    
g(10,19)
g(w=19,v=10)


# Practice Problem: Use the filter() function combined with a lambda to extract all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x:x%2!=0,numbers))
print(even)


# Practice Problem: Use the map() function and a lambda to double every element in the list [1, 2, 3, 4, 5].

num = [1, 2, 3, 4, 5]

m = list (map(lambda x:x+x,num) )
print(m)

# Practice Problem: You have a list of tuples representing students and their grades: [("Alice", 88), ("Bob", 75), ("Charlie", 92)]. Use the sorted() function and a lambda to sort this list based on the grades (the second element) in ascending order.

students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]

st = sorted ( students, key=lambda student:students[0])
print(st)

# Practice Problem: Write a function apply_operation(func, x, y) that takes another function (func) and two numbers (x, y) as arguments. It should return the result of calling func(x, y). Show how this works by passing in different operations like addition and multiplication.

def op(func,x,y):
    return func(x,y)
def add(x,y):
    print(x+y)
op(add,2,6)