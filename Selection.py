def selection(arr):
    print(arr)
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i] ,arr[min_index] = arr[min_index],arr[i]
    print(arr)

arr = [23,12,78,11,91,81,40]
selection(arr)