def insertion(arr):
    print(arr)
    for i in range(1,len(arr)):
        key = arr[i]
        j= i -1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    print(arr)

arr = [23,12,78,11,91,81,40]
insertion(arr)