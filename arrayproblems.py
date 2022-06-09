#negative numbers to one side



def negNum(arr):
    neg = set()
    pos = set()
    for i in arr:
        if i < 0:
            neg.add(i)
        elif i >= 0:
            pos.add(i)
    
    final = list(neg.union(pos))
    return final

arr = [1, -1, 3, 2, -7, -5, 11, 6]
print(negNum(arr))