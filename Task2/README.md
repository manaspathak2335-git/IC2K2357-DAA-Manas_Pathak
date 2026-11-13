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

Program-2:2D Array operations

Aim: Build a program that lets the user work with a 2D array (list of lists) and supports: 

● Insert a new row at a given position 

● Delete a row at a given position 

● Search for a value across the entire 2D array, returning the row and column where it was found, or a not-found message 

● Rotate the entire 2D array 90 degrees clockwise Display the array in proper row-by-row format after every operation.

Logic:This program initializes a 2D array (list of lists) from validated user input and sequentially performs core matrix operations: row insertion and row deletion shift outer list references at a specified index, while 2D linear search uses nested loops to scan across rows and columns for a target coordinate. Finally, it executes a 90-degree clockwise rotation by combining matrix transposition and row reversal—reading each column from bottom to top into a new row—and prints the formatted grid after every step.

Sample Output:

Enter number of rows: 2

Enter number of columns: 3

Enter 3 space-separated elements for row 0: 1 2 3

Enter 3 space-separated elements for row 1: 4 5 6

Initial 2D Array:

[1, 2, 3]

[4, 5, 6]

Enter row position (index) to insert at: 2

Enter 3 space-separated elements for the new row: 7 8 9

2D Array after inserting row at index 2:

[1, 2, 3]

[4, 5, 6]

[7, 8, 9]

Enter row position (index) to delete: 5

Invalid row position for deletion.

[1, 2, 3]

[4, 5, 6]

[7, 8, 9]

Enter value to search in the 2D array: 5

Value 5 found at Row 1, Column 1.

Current 2D Array:

[1, 2, 3]

[4, 5, 6]

[7, 8, 9]

2D Array after rotating 90 degrees clockwise:

[7, 4, 1]

[8, 5, 2]

[9, 6, 3]

Program-3: Sparse Matrix Operations

Aim: Write a program that: 

● Converts a full 2D matrix (list of lists) into its sparse triple representation 

● Reconstructs the full matrix back from a sparse triple representation 

● Adds two matrices while both are in sparse form, producing a result that is also in sparse form, without converting either input back to a full matrix first 

● Displays both the sparse form and the reconstructed full form, so the two can be compared 

Logic:This program takes user input to create two 2D matrices, converts them into 3-tuple sparse triple representations, and reconstructs them back into full matrices. It then performs direct addition on the matrices while they are still in sparse form using a two-pointer merge technique, displaying both the sparse and reconstructed full results for comparison.

Sample Output:

--- Enter details for Matrix 1 ---

Enter number of rows for Matrix 1: 3

Enter number of columns for Matrix 1: 3

Enter 3 space-separated elements for row 0: 1 0 0

Enter 3 space-separated elements for row 1: 3 0 2

Enter 3 space-separated elements for row 2: 0 2 0

Full 2D Form of Matrix 1:

[1, 0, 0]

[3, 0, 2]

[0, 2, 0]

Sparse Triple Representation of Matrix 1:

Row	Col	Value

----------------------

3	3	4  <-- (Header: Total Rows, Cols, Non-Zero Count)

0	0	1

1	0	3

1	2	2

2	1	2

Reconstructed Full 2D Form of Matrix 1 (from Sparse):

[1, 0, 0]

[3, 0, 2]

[0, 2, 0]

--- Enter Second Matrix for Sparse Addition ---

--- Enter details for Matrix 2 ---

Enter number of rows for Matrix 2: 3

Enter number of columns for Matrix 2: 3

Enter 3 space-separated elements for row 0: 1 0 1

Enter 3 space-separated elements for row 1: -1 0 -1

Enter 3 space-separated elements for row 2: 0 0 0

Full 2D Form of Matrix 2:

[1, 0, 1]

[-1, 0, -1]

[0, 0, 0]

Sparse Representation of Matrix 2:

Row	Col	Value

----------------------

3	3	4  <-- (Header: Total Rows, Cols, Non-Zero Count)

0	0	1

0	2	1

1	0	-1

1	2	-1

Result of Addition (Sparse Triple Form):

Row	Col	Value

----------------------

3	3	5  <-- (Header: Total Rows, Cols, Non-Zero Count)

0	0	2

0	2	1

1	0	2

1	2	1

2	1	2

Result of Addition (Reconstructed Full 2D Form):

[2, 0, 1]

[2, 0, 1]

[0, 2, 0]

Section D: Space Optimization Analysis

1. Space Used by Representations
  
   Full 2D representation: O(mXn) to store all entries across m rows and n columns.

   Sparse triple representation: O(k) to store only the k non-zero triplets plus one header entry.

2. Actual Element Counts (Test Results)
  
   Matrix A (6X6 with 80% zeroes i.e 7 non-zero elements):

   Full 2D representation: 36 elements (6X6).

   Sparse triple representation: 8 entries (1 header + 7 non-zero triplets).

   Matrix B (6X6 with < 20% zeroes i.e 30 non-zero elements):

   Full 2D representation: 36 elements (6X6).

   Sparse triple representation: 31 entries (1 header + 30 non-zero triplets).

   3. Space-Saving Threshold
  
      Threshold: roughly 33% elements

      Reasoning: Each triplet entry in a sparse representation stores 3 values (row, col, value), whereas a full representation stores 1 value per position. If the number of non-zero elements $k$ exceeds one-third of the total elements (mXn), storing 3 integers per non-zero element requires more data than the single grid slots of the full matrix.

 4. Real-World Sparse Matrix Situation
    
Example: Web Search Engine Term-Document Matrices.

Why most entries are zero: Most web pages (documents) contain only a tiny fraction of the hundreds of thousands of words (terms) available in a global vocabulary, resulting in mostly zero entries for unmentioned words.
