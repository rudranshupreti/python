#  Write a Python program to access the value associated with the key 'history' from a dictionary nested within a larger data structure.
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}

history_grade = student["grades"]["history"]
print("History grade:", history_grade)
# Write a Python program to create a dictionary from a list of keys, assigning the same default value to every key.

keys = ["math", "science", "english", "history"] 
default = 0

this = dict.fromkeys(keys,default)
print(this)