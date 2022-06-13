firstline = input().split(" ")


arrLen = int(firstline[0])
k = int(firstline[1])
arr = []
while len(arr) < arrLen:
    arr = input().split(" ")

# we'll use a hashmap/array of some sort to store the array. then we will add the indexes of k to that array
# sort it, and return the middle index. Done!

new = {}
for i in range(len(arr)):
    new[i] = int(arr[i])

s = set()
for i in range(len(arr)):
    if arr[i] == k:
        s.add(i)

print(s)


# new_arr = list(new.keys())
# print(new_arr)

# mid = len(new_arr) // 2
# print(new_arr[mid])




# new_arr = []
# if new.get(i) == k:
#     new_arr.append(i)
# print(new_arr)


# if firstline[1] in arr:
#     print(arr.index(firstline[1]))
# else:
#     print('K is not present')
