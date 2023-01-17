import  math
def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr


def bucket(arr):
    print(arr)
    no_of_element = len(arr)
    no_of_bucket = int(math.sqrt(no_of_element))
    max_element = max(arr)
    res_arr = []
    for i in range(no_of_bucket):
        res_arr.append([])
    for i in arr:
        index_bucket = math.ceil((i/max_element)*no_of_bucket)
        res_arr[index_bucket-1].append(i)
    
    print(res_arr)
    
    for i in range(len(res_arr)):
        res_arr[i] = insertionsort(res_arr[i])

    print(res_arr)    
    k = 0
    for i in range(len(res_arr)):
        for j in range(len(res_arr[i])):
            arr[k] = res_arr[i][j]
            k  +=1
    print(arr)


    

arr = [23,12,78,11,91,81,40]
bucket(arr)