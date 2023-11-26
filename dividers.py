# input
# 3,4,2,1,5,8
# 2
# output - 3,1,5

list = input()
num = int(input())

arr = list.split(",")
arr2 = []
for n in arr:
    if not int(n) % num == 0:
        arr2.append(n)


print(arr2)
        