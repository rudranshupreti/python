# Practice Problem: Given a list of integers, move all even numbers to the beginning of the list and all odd numbers to the end.
l = [1, 2, 3, 4, 5, 6]
e=[]
o=[]
for i in l:
    if i %2==0:
        e.append(i)
    if i %2!=0:
        o.append(i) 
        
print(e+o)


# Practice Problem: Given a list and an integer k, rotate the list to the left by k positions. For example, if k=2, the first two elements move to the end of the list.

nums = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    f = nums.pop(0)
    nums.append(f)
print(nums)


# Practice Problem: Write a program to count the frequency of each word in a given string.

text = "apple banana apple orange banana apple"
words= text.split()
fe ={}

for i in words:
    if i in fe:
        fe[i]+=1
    else:
        fe[i] =1
print(fe)

# Practice Problem: Write a program to check if a number is a “Perfect Number.” A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.

num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")