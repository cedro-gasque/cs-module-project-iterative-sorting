def linear_search(arr, target):
    # Your code here
    for i, n in enumerate(arr):
        if n == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    array = arr[:]
    while True:
        mid = len(array)//2
        if len(array) <= 1:
            break
        elif target == array[mid]:
            return arr.index(target)
        elif target < array[mid]:
            array = array[:mid]
        else:
            array = array[mid:]
    return -1  # not found
