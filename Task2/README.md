Section A: Concept Check

1. In Python, a 1D array is commonly implemented using a "LIST".

2. Inserting an element at the beginning of a list requires shifting "ALL EXISTING" elements, making it an "O(n)" operation.

3. Deleting an element from the middle of a list requires shifting all elements "TO THE RIGHT OF" it, to fill the gap.

4. A left rotation by k positions moves the first k elements to the "END" of the array.

5. Linear search checks elements "SEQUENTIALLY", while binary search requires the array to be "SORTED" first.

6. A sparse matrix stores only "NON-ZERO" elements, along with their "ROW" index and "COLUMN" index.

7. The standard triple format for a sparse matrix entry is ("ROW,COLUMN,VALUE").

Program-1: 1-D Array Operations

Aim: Build a program that lets the user work with a 1D array (Python list) and supports:

● Insert a value at a given index 

● Delete a value at a given index 

● Linear search for a value, returning its index or a not-found message 

● Rotate the array left by k positions, and rotate right by k positions Print the array after every operation so changes are visible. 

Logic: This program initializes a 1D dynamic array (Python list) from user input and performs core operations directly in memory: insertion and deletion manually shift subsequent elements right or left to create or close index gaps, linear search sequentially scans indices until a target matches, and left/right rotations use modulo arithmetic (k % n) and slice assignment (arr[:]) to cyclically wrap elements around the array boundaries. All operations update and print the list in-place inside a menu-driven loop so every state change is immediately visible.

Sample Output:

Enter elements of array as space seprated values:10 20 30 40 50

Raw Array: [10, 20, 30, 40, 50]

Inserting element at given index:

Enter index: 8

Enter value to insert: 60

Error: Index 8 is out of bounds for insertion (valid: 0 to 5).

Array after insertion: [10, 20, 30, 40, 50]

Deleting element from given index

Enter index to delete: 0

Array after deletion: [20, 30, 40, 50]

Searching a given element

Enter value to search: 40

Linear Search: Value 40 found at index 2. | Array: [20, 30, 40, 50]

Rotating array k elements to left

Enter k (positions to rotate left): 2

Rotated Left by 2 position(s) -> Array: [40, 50, 20, 30]

Rotating array k elements to right

Enter k (positions to rotate right): 7

Rotated Right by 3 position(s) -> Array: [50, 20, 30, 40]

Final array: [50, 20, 30, 40]
