def search_index(arr, low, high):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid]==1 and arr[mid+1]==0:
            return mid
        if arr[mid] == 0:
            return search_index(arr, low, mid - 1)
        else:
            return search_index(arr, mid+1, high)
    else:
        return 0
a=[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0]
print(search_index(a,0,len(a)-1))