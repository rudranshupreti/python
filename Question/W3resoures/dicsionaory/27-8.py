"""Write a Python script to sort (ascending and descending) a dictionary by value.

a = {"a": 1, "b": 32, "c": 44}
ac = dict(sorted(a.items(), key=lambda item: item[1]))
print(ac)
dc = dict(sorted(a.items(), key=lambda item: item[1], reverse=True))
print(dc)"""

"""Write a Python program to add a key to a dictionary.
a = {"a": 1, "b": 32, "c": 44}
h = a.update({"d": 123})
print(a)"""

"""Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
d4 = {}
for d in (dic3, dic2, dic1):
    d4.update(d)
print(d4)"""

"""Write a Python script to check whether a given key already exists in a dictionary.
student = {"name": "Aman", "age": 20}
for name in student:
    print("yes")"""
