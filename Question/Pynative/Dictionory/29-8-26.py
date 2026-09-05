# Write a Python program to create a new dictionary containing only a specified subset of keys from an existing dictionary.
user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"} 
extract = ["id", "username", "email"]
Output ={'id': 42, 'username': 'jdoe', 'email': 'jdoe@example.com'}
for i in user :
    print (i)