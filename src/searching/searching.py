def linear_search(arr, target):
    for i in range(len(arr - 1)):
    if i == target:
        return 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = ((end+start)/2) + 1
    if(target < arr[mid]):
       end = mid
    elif(target > arr[mid]):
       start = mid
    else:
        return 1
    # Your code here


    return -1  # not found
