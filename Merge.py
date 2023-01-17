def divide(arr,l,h):
    
    if l == h:
        return 
    m = (l + h) // 2
    # print(arr[l:m+1])
    # print(arr[m+1:h+1])
    print(l,m,h)
    divide(arr,l,m)
    divide(arr,m+1,h)
    merge(arr,l,m,h)
def merge(arr,l,m,h):
    n1 = (m-l)+1
    n2 = (h-m)
    L = [0] * n1
    R = [0]* n2
    for i in range(n1):
        L[i] = arr[l+i]
    for j in range(n2):
        R[j] = arr[m+1+j]
    # print(L,R)
    k = l
    i = 0
    j = 0
    while i<n1 and j <n2:
        if L[i]<R[j]:
            arr[k] = L[i]
            i +=1
        else:
            arr[k] = R[j]
            j +=1
        k +=1
    while i<n1:
        arr[k] = L[i]
        i =i+1
        k = k+1
    while j<n2:
        arr[k] = R[j]
        j = j+1
        k = k+1
    
arr = [23,12,78,11,91,14,19,76]
divide(arr,0,len(arr)-1)
print(arr)
