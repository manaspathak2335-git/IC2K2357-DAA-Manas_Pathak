# Program to take a 1D array from user input and sort it in ascending order 
# using the Selection Sort algorithm by repeatedly finding the minimum element.

def input_array():
    arr = [int(x) for x in input("Enter array elements separated by spaces: ").split()]
    print(f"Initial Unsorted Array: {arr}\n")
    return arr


def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        # Assume the first element of the unsorted region is the minimum
        min_idx = i
        
        # Scan the rest of the unsorted region to find the true minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of the unsorted region
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    print(f"Sorted Array (Selection Sort): {arr}")
    return arr


arr = input_array()
selection_sort(arr)
