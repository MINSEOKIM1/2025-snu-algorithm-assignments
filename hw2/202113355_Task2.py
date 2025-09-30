import random

def insertion_sort(arr):
    # arr[0] is already sorted. so we start from arr[1]
    for i in range(1, len(arr)):
        # traverse the subarray before arr[i] to find the correct insertion spot
        for j in range(0, i):
            # if we find a correct spot for insertion, insert it!
            if arr[i] < arr[j]:
                arr1 = arr[:j]
                arr2 = arr[j:i]
                arr3 = arr[i+1:]

                arr = arr1 + [arr[i]] + arr2 + arr3
                break

    return arr

# helper function for merge sort!
# take two sorted arrays and merge them into a single sorted array
def merge(arr1, arr2):
    i = j = 0
    result = []

    # traverse both arrays until the end of one is reached
    while i < len(arr1) and j < len(arr2):
        # append the smaller element to the result array first
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result = result + arr1[i:] + arr2[j:]

    return result

def merge_sort(arr):
    # base case for recursion
    if len(arr) <= 1 :
        return arr
    
    middle = len(arr) // 2

    # apply recursion on both arrays and obtain two sorted arrays
    l_arr = merge_sort(arr[:middle])
    r_arr = merge_sort(arr[middle:])

    # merge two sorted arrays
    return merge(l_arr, r_arr)

def quick_sort(arr):
    # base case for recursion
    if len(arr) <= 1:
        return arr
    
    # randomly pick a pivot
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    l_arr = []
    r_arr = []

    # split the array into two arrays:
    #   one containing elements smaller than the pivot,
    #   the other containing elements greater than the pivot
    for i in range(len(arr)):
        if i != pivot_index:
            if arr[i] < pivot:
                l_arr.append(arr[i])
            else:
                r_arr.append(arr[i])
    
    # apply quick sort recursively on both two arrays
    l_arr = quick_sort(l_arr)
    r_arr = quick_sort(r_arr)

    # concatenate two arrays and pivot => what we wanted!
    result = l_arr + [pivot] + r_arr

    return result
    

# test code


test1 = list(range(10))

random.shuffle(test1)

print(test1)

print(quick_sort(test1))
