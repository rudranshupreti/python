# Practice Problem: Print a downward half-pyramid pattern using stars (*).
for i in range(6):
    for j in range(i,6):
        print("*",end=" ")
    print()
    
    
# Practice Problem: Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.
# isse hum accumulator pattern ko sikhte hhe mean har bar jo ititattion hota he vo usse store krta he 

def accu (ex,bas):
    result = 1
    for i in range(ex):
        result = bas*result
    print (result)

# Practice Problem: Write a program that takes two separate dictionaries and merges them into one single dictionary.
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
final= dict1|dict2
print(final)


# Practice Problem: Take two lists and find the elements that appear in both. Use Sets to perform the operation.

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

a = set(list_a)
b = set(list_b)
anw = a & b
print(anw)

# Practice Problem: Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.
words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for i in words:
    print(i,-len(i),end=" ")


# Practice Problem: Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.
text = "apple banana apple cherry banana apple"
word = text.split()
count= {}
for i in word:
    if i in count:
        count[i] += 1
    else: 
        count[i] = 1
print(count)
    