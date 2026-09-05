# Practice Problem: Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number foun 
fn = []
for num in range(2,21):
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
    if prime:
        fn.append(num)
for i in range(1,len(fn),2):
    print(i)
student = {}

# Practice Problem: Create a dictiona/ry where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).


for i in range(1, 11):
    student[i] = i * i

print(student)

# Practice Problem: Ask the user for a sentence. Replace every empty space in that sentence with an underscore (_) and print the final result.

input = "I love coding in Python"
print(input.replace(" ",'_'))     


# Practice Problem: Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.
im = "Python3"
for i in (im):
    if i.isdigit():
        print(True)