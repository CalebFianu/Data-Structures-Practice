#Recursively...
def binsearch(A, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return binsearch(A, key, low, mid-1)
        else:
            return binsearch(A, key, mid+1, high)
   
A = [13,24,45,67,78,99]
key = input("Enter the element you are searching for: ")
found = binsearch(A, int(key), 0, 6)
print("Element " + key + " is in the array: ", found) 