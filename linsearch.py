def linsearch(A, key):
    position = 0
    flag = False
    while position < len(A) and not flag:
        if A[position] == key:
            flag = True
            break
        else:
            position = position + 1
    return flag      
        

A = [1,2,3,4,5]
key = input("Enter the element you are searching for: ")
found = linsearch(A, int(key))
print("Element " + key + " is in the array: ", found)