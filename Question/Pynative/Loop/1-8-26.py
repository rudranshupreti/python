# Practice Problem: Given a nested list (a list containing other lists), write a program to “flatten” it into a single list containing all the individual elements.
t = [[10, 20], [30, 40], [50, 60]]
l=[]
for i in t:
  for j in i:
      l.append(j)
print(l)


# Practice Problem: Given a 2D list (matrix), find the row and column index of a target value.

matrix = [[10, 20], [30, 40], [50, 60]]
target = 30
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(i,j)