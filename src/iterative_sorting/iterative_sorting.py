# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        j = cur_index
        for j in range(j, len(arr)):
            if arr[j] < arr[cur_index]:
                temp_variable = arr[cur_index]
                arr[cur_index] = arr[j]
                arr[j] = temp_variable 

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, (len(arr))):
        for j in range(0, (len(arr))):
            if arr[i] < arr[j]:
                temp_variable = arr[i]
                arr[i] = arr[j]
                arr[j] = temp_variable

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

We need the plus one because we need to also store the max value as an element in the array/list

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    appropriate_max = maximum+1
    bucket_list = [0] * appropriate_max

    for j in range(0, len(bucket_list)):
        print(bucket_list[j])

    for i in range(0, len(bucket_list)):
        print("This is the value of i:", i)
        print("This is the value of arr[i]:", arr[i])
        bucket_list[arr[i]] = bucket_list[arr[i]] + 1

    for j in range(0, len(bucket_list)):
        print("test")
        print(bucket_list[j])

    # Your code here

    return arr


array = [2, 4, 5, 6, 7, 1, 3, 4, 9]

counting_sort(array, 9)