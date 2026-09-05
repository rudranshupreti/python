"""Write a Python program to create a histogram from a given list of integers.
def check(n):
    for item in n:
        output = ""
        time = item

        while time > 0:
            output += "*"
            time -= 1
        print(output)


check([1, 3, 3, 4])"""

"""Write a Python program that concatenates all elements in a list into a string and returns it
def convert(num):
    output = ""
    for item in num:
        output += str(item)
    return output
print(
    convert(
        [
            1,
            2,
            3,
            32,
        ]
    )
)
  """
"""Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]


def check(num):
    for item in num:
        if item == 237:
            print(item)
            break
        elif item % 2 == 0:
            print(item)


check(
    [
        386,
        462,
        47,
        418,
        907,
        344,
        236,
        375,
        823,
        566,
        597,
        978,
        328,
        615,
        953,
        345,
        399,
        162,
        758,
        219,
        918,
        237,
        412,
        566,
        826,
        248,
        866,
        950,
        626,
        949,
        687,
        217,
        815,
        67,
        104,
        58,
        512,
        24,
        892,
        894,
        767,
        553,
        81,
        379,
        843,
        831,
        445,
        742,
        717,
        958,
        743,
        527,
    ]
)
  """
"""Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
def check(l1, l2):
    for num1 in l1:
        if num1 not in l2:
            print(num1)
check(["White", "Black", "Red"], ["Red", "Green"])
  """
