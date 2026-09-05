# Problem Statement: Write a Python program to remove a specific key from a dictionary, retrieve all key-value pairs, and check whether a given key 
car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
car.pop("color")
print (car.items())

# Problem Statement: Write a Python program to create a dictionary by mapping two equal-length lists, one containing keys and the other containing values.

keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]

result = dict(zip(keys,values))
print(result)

# Problem Statement: Write a Python program to combine two dictionaries into a single dictionary. If both dictionaries share a key, the value from the second dictionary should take precedence.

dict1 = {"a": 1, "b": 2} 
dict2 = {"b": 3, "c": 4}
m = dict1|dict2
print(m)

# Problem Statement: Write a Python program to retrieve a specific value from a dictionary that is nested inside another dictionary.

person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
print(person["address"]["city"])


# Problem Statement: Write a Python program to access the value associated with the key 'history' from a dictionary nested within a larger data structure.
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
print(student["grades"]["history"])

