# Write a Python program to remove multiple specific keys from a dictionary in one operation.
product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"} 
keys = ["stock", "warehouse"]

for i in product.copy():
    if i in keys:
        product.pop(i)
print(product)

# Write a Python program to verify whether a specific value is present anywhere in a dictionary.
roles = {"alice": "admin", "bob": "editor", "carol": "viewer"} 

for role in["manager","editor"]:
    if role in roles.values():
        print(role, 'yes')
    else :
        print(role,"no")

# Write a Python program to calculate the total of all numerical values stored in a dictionary
expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
m=0
for i in expenses.values():
    m = m+i
print(m)
