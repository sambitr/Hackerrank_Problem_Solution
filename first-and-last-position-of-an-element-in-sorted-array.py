def leftindex(array, key, n):
    min, ans = 0, -1
    max = n-1
    mid = min + (max-min) // 2
    while(min <= max):
        if ( key == array[mid]):
            ans = mid
            max = mid-1
        elif( key > array[mid]):
            min = mid + 1
        else:
            max = mid - 1
        
        mid = min + (max-min) // 2

    return(ans)
def rightindex(array, key,n):
    min, ans = 0, -1
    max = n-1
    mid = min + (max-min) // 2
    while(min <= max):
        if ( key == array[mid]):
            ans = mid
            min = mid+1
        elif( key > array[mid]):
            min = mid + 1
        else:
            max = mid - 1
        
        mid = min + (max-min) // 2

    return(ans)

def firstAndLastPosition(arr, n, k):
    # Write your code here
    result = []
    left_index = leftindex(arr, k, n)
    right_index = rightindex(arr, k, n)
    result.append(left_index)
    result.append(right_index)
    return(result)
    
    pass
