"""Write a Python program to calculate the length of a string.
h = "hello sir"
print(len(h))"""

"""Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1
str = " hello sir"
check = {}
for char in str:
    if char in check:
        check[char] += 1
    else:
        check[char] = 1
for key, value in check.items():
    print(f"{key}:{value}")
"""
"""Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String


def str(af):
    if len(af) >= 2:
        print(af)
    else:
        positive = af[0:2]
        negative = af[-2:]
        return print(f"{positive}{negative}")


str("he")"""
""" Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t


def check(str):
    fl = str[0:]
    for fl in str:
        if fl in str:
            change = str.replace(fl, "$")
            return print(change)
        else:
            return print(str)


check("hello hi")


# ye ese bhi ho skta tha direct method lageke
def change_string(text):
    first_char = text[0]
    rest = text[1:].replace(first_char, "$")
    return first_char + rest


print(change_string("restart"))"""

"""Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz


def make(a, b):
    a1 = b[:2] + a[-2:]
    b1 = a[:2] + b[-2:]
    return print(a1 + " " + b1)


make("hello", "bye")"""
"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'


def check(af):
    if len(af) <= 3:
        return print(af)
    elif af[-3:] == "ing":
        af += "ly"
        return print(af)
    elif af[-3:] != "ing":
        af += "ing"
        return print(af)


check("hello")"""

"""Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'


def check(al):
    nt = al.find("not")
    pr = al.find("poor")
    change = al.replace(al[nt : pr + 4], "good")# isme +4 ka use isilliye kiya he kyoki find ke time pe vo string ki starting value leta he jesse abhi ke liye vo 22 to usse equal krne ke liye mujhe usme 4 add kiya he taki replace ka time pe usme  last vale se kr paoo 
    
    print(change)


check("The lyrics is not that poor!")"""

"""Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9"""
