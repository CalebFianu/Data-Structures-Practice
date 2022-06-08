firstline = input().split(" ")
N = int(firstline[0])
K = int(firstline[1])

arr = []
while len(arr) < N:
    arr = list(map(int, input().split(" ")))

for i in range(len(arr)-1,-1,-1):
    print(arr[i], end = " ")