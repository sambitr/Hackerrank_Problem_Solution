# https://www.codingninjas.com/codestudio/problem-details/first-and-last-position-of-an-element-in-sorted-array_1082549

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


array = [1,2,3,3,5]
#[1,2,3,3,5]
#[0,1,1,5]
key = 4
n = len(array)
left_index = leftindex(array, key, n)
right_index = rightindex(array, key, n)
result = []

result.append(left_index)
result.append(right_index)
print(result)
