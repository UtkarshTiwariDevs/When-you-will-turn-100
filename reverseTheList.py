"""
print("enter 10 numbers")
inpList = []
for i in range(0,10):
    ele = int(input())
    inpList.append(ele)  #or I made list on my own
"""
lst = [56, 87, 90, 234, 657, 99, 86, 909, 96, 665]
lst.sort()
print(lst)

# method 1
method1Lst = lst.copy()
method1Lst.reverse()
print(method1Lst)

# method 2
var1 = lst.copy()
method2Lst = var1[::-1]
print(method2Lst)

# method 3
method3Lst = lst.copy()
for i in range(0, len(method3Lst)//2):
    method3Lst[i],method3Lst[len(method3Lst)-1-i]=method3Lst[len(method3Lst)-1-i],method3Lst[i]
print(method3Lst)