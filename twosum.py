def find_num(arr, target):
    index1 = 0
    index2 = len(arr) - 1

    while (index1 < index2):
        cur = arr[index1] + arr[index2]
        if cur == target:
            return True
        elif cur > target:
            index2 = index2 - 1
        else:
            index1 = index1 + 1
    return False

arr = [1,8,3,9,5,6,2]
arr2 = [1,2,3,4,5]
print(find_num(arr2,10))