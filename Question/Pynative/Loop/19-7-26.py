# Practice Problem: Write a program that takes a string and reverses it using a for loop. While Python’s [::-1] shortcut is famous, reversing a string manually is a classic way to understand how sequences are constructed
l = "python"
m =""
for i in(l):
    m = i+m
    
print(m)

# Practice Problem: Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.

t ="Loops are Fun!"
v = "aeiou"
l =0
c=0
for i in  t.lower ():
    if i.isalpha():
        if i in v:
            l+=1 
        else:
            c+=1                             
print(l,c) 

# Practice Problem: Write a program to count the total number of digits in a given integer using a while loop.

i = 75869
m=0
while i !=0:
    i=i//10
    m= m+1
    
print(m)

# Practice Problem: Write a program to reverse a given integer number (e.g., 76542 should become 24567).
n=0
t=234562356
while t >0:
    dt =t%10
    n =(n*10)+dt
    t=t//10
print(n)

# Practice Problem: Write a program to find the largest and smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).
s=2
m=0 
k=2345125
while k>0:
    dt =k%10
    if dt >  m:
        m=dt          
    if dt <  s:
        s=dt
    k=k//10
print(s,m)


