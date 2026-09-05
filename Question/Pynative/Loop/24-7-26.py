# Practice Problem: Given a dictionary of student scores, create a new dictionary that only includes students who scored above a certain threshold (e.g., 75).
scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60} 
threshold = 75
passing={}
for name ,scores in scores.items():
    if scores>= threshold:
        passing[name]= scores
print(passing)


# Practice Problem: Given two lists, find the elements that appear in both. Do not use Python’s built-in set().intersection() method.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
m=[]
for i in a:
    for j in b:
        if i == j:
            m.append(i)
print(m)


# Practice Problem: Write a program to remove all duplicate values from a list using a loop, maintaining the original order of elements.

l =[1, 2, 2, 3, 4, 4, 4, 5]
k=[]
for i in l :
    if i not in k:
        k.append(i)
        
print(k)