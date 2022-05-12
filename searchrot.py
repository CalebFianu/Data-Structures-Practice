def search(arr, target):
    start = 0
    end = len(arr)
    leftnum = arr[0]
    rightnum = arr[-1] #last element in an array

    while (start <= end):
        mid = (start + end)//2

        if arr[mid] == target:
            return True
        else:
            if arr[mid] > rightnum:
            #you are on the left of the line
                if target >= leftnum and target < arr[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
            #you are on the right side of the line
                if target <= rightnum and target > arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
    return False

arr = [5,4,3,0,1,2]
print(search(arr, 9))