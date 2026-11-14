# Program to take a sorted 1D array from user input and implement iterative binary search 
# to locate an existing target value and a non-existing target value, returning the index or -1.

def input_sorted_array():
    arr = [int(x) for x in input("Enter sorted array elements separated by spaces: ").split()]
    arr.sort()  # Ensure the array is sorted for binary search
    print(f"Sorted Array: {arr}\n")
    return arr

def binary_search(arr):
    target = int(input("Enter target element to find:"))
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print(f"Target {target} found at index: {mid}\n")
            return mid
        elif arr[mid] < target:
            low = mid + 1  # Discard left half
        else:
            high = mid - 1  # Discard right half

    print(f"Target {target} not found. Returned: -1\n")
    return -1

arr=input_sorted_array()
binary_search(arr)
