#Iteratively...
def binsearch(A, key):
    low = 0 
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2 #integer division
        if key == A[mid]:
            return True
        elif key < A[mid]:
            high = mid - 1
        else: # (key > A[mid])
            low = mid + 1
    return False

A = [1,2,3,4,5,6]
key = input("Enter the element you are searching for: ")
found = binsearch(A, int(key))
print("Element " + key + " is in the array: ", found) 