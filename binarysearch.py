def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = (start + end) // 2
        if arr[mid] < target:
            #mid is smamller, search in the right
            start = mid + 1
        elif arr[mid] > target:
            #mid is larger, search in the left
            end = mid - 1
        else:
            return True
    return False

arr = [1,2,3,4,5,6]
print(binary_search(arr, 9))

