#  Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, 
# return their product; otherwise, return their sum.
def podsum(a,b):
    if a*b <= 1000:
      return  a*b
    else: 
      return a+b

print(podsum(20,30))

print(podsum(40,30))