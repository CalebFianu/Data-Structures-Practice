def bubblesort(A):
    for i in range(len(A)-1, 0, -1): #where i is the pass
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            
A = [4,2,3,7,10]
print("Original Array: ", A)
bubblesort(A)
print("Sorted Array: ", A)