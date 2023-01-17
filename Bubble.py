def bubble(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
            
    
arr = [23,12,78,11,91,81,40]
bubble(arr)