import numpy as np

"""to make simple array
y = np.array([1, 1, 2, 3, 4, 3])
print(y)
print(type(y))"""

# make a Array with input by user
L = []
for i in range(1, 5):
    int_i = input("enter:")
    L.append(int_i)
print(np.array(L))
