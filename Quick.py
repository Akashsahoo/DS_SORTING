def partition(arr,lb,ub):
    pivot = arr[ub]
    i = lb-1
    for j in range(lb,ub):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[ub] = arr[ub],arr[i+1]
    return i+1

def quicksort(arr,lb,ub):
    if lb<ub:
        end = partition(arr,lb,ub)
        quicksort(arr,lb,end-1)
        quicksort(arr,end+1,ub)


arr = [23,12,78,11,91,14,12,19,76,1]
print(arr)
quicksort(arr,0,len(arr)-1)
print(arr)