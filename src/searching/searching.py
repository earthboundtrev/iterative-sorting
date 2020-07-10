import math

def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1



# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    if(len(arr)-1)%2 == 0:
        mid = math.ceil((end+start)/2+1)
    else:
        mid = math.ceil((end+start)/2-1)

    if(target < arr[mid]):
       end = mid
    elif(target > arr[mid]):
       start = mid
    else:
        return mid

    return -1  # not found
