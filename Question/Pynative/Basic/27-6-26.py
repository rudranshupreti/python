def reverse(x):
    dump = ""
    for i in range(len(x) - 1, -1, -1):
        dump += x[i]
    return dump
hello = "hello"
print(reverse(hello))   





list = [1,2,3,23,4,2]
list.sort()
print (  f"LIST MINl {list[1]}" )
print (  f"LIST MIN {list[-1]}")


print(set(list))



list1 = [2,2,3,23,4,2]

a = list1[-1]
b = list1[1]
if a == b:
    print("true")
else:
    print("false")
    


dump = []
for i in range(len(list)):
    # if i % 5 == 0:
    dump.append(i)
    print(i)