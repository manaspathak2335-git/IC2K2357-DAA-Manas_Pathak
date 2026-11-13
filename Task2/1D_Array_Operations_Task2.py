#Program to perform 1-D operations on array

def input_array():
    raw_input = input("Enter elements of array as space seprated values:").strip()
    if not raw_input:
        arr=[]
    else:
        arr = [int(x) for x in raw_input.split()]
    return arr

def insert_at_index(arr):
    print("Inserting element at given index:")
    index = int(input("Enter index: "))
    value = int(input("Enter value to insert: "))
    if index < 0 or index > len(arr):
        print(f"Error: Index {index} is out of bounds for insertion (valid: 0 to {len(arr)}).")
        return arr
    arr.insert(index,value)
    return arr

def delete_at_index(arr):
    print("Deleting element from given index")
    if len(arr) == 0:
        print("Error: Cannot delete from an empty array.")
        return arr
    index = int(input("Enter index to delete: "))
    if index < 0 or index >= len(arr):
        print(f"Error: Index {index} is out of bounds for deletion (valid: 0 to {len(arr) - 1}).")
        return arr
    arr.pop(index)
    return arr

def linear_search(arr):
    print("Searching a given element")
    target = int(input("Enter value to search: ")) 
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Linear Search: Value {target} found at index {i}. | Array: {arr}")
            return
    print(f"Linear Search: Value {target} not found in the array. | Array: {arr}")

def rotate_left(arr):
    print("Rotating array k elements to left")
    k = int(input("Enter k (positions to rotate left): "))
    n = len(arr)
    if n == 0:
        print("Array is empty.")
        return arr

    k = k % n
    arr = arr[k:] + arr[:k]
    print(f"Rotated Left by {k} position(s) -> Array: {arr}")
    return arr

def rotate_right(arr):
    print("Rotating array k elements to right")
    k = int(input("Enter k (positions to rotate right): "))
    n=len(arr)
    if n == 0:
        print("Array is empty.")
        return arr

    k = k % n  
    arr[:] = arr[n - k:] + arr[:n - k]  
    print(f"Rotated Right by {k} position(s) -> Array: {arr}")
    return arr

    
arr=input_array()
print("Raw Array:",arr)
arr = insert_at_index(arr)
print("Array after insertion:",arr)
arr = delete_at_index(arr)
print("Array after deletion:",arr)
linear_search(arr)
arr = rotate_left(arr)
arr = rotate_right(arr)
print("Final array:", arr)

