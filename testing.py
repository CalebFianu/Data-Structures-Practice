firstline = input().split(" ")
#N = firstline[0]
#K = firstline[1]

arrLen = int(firstline[0])
arr = []
while len(arr) < arrLen:
    arr = input().split(" ")


# print(firstline[::-1])
if firstline[1] in arr:
    print(arr.index(firstline[1]))
else:
    print('K is not present')