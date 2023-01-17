def shell(arr):
    print(arr)
    gap = (len(arr)-1)//2
    # gap = len(arr) -1
    while gap >0:
        j = gap
        while j <len(arr):
            i = j-gap
            while i >=0:
                if(arr[i+gap]>arr[i]):
                    break;
                else:
                    arr[i+gap],arr[i] = arr[i],arr[i+gap]
                i = i-gap
            j =j+1
        gap = gap//2
        # gap = gap-1
    print(arr)


arr = [23,12,78,11,91,81,12,40]
shell(arr)