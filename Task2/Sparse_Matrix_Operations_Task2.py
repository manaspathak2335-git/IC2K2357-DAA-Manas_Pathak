# Program to take user input for 2D matrices, convert them into 3-tuple sparse representation 
# (row, column, value), reconstruct full 2D matrices from sparse form, and add two sparse 
# matrices directly in sparse form to compare both representations.

def display_full_matrix(matrix):
    if not matrix:
        print("Matrix is empty.\n")
        return
    for row in matrix:
        print(row)
    print()


def display_sparse_matrix(sparse):
    print("Row\tCol\tValue")
    print("-" * 22)
    for idx, entry in enumerate(sparse):
        if idx == 0:
            print(f"{entry[0]}\t{entry[1]}\t{entry[2]}  <-- (Header: Total Rows, Cols, Non-Zero Count)")
        else:
            print(f"{entry[0]}\t{entry[1]}\t{entry[2]}")
    print()


def get_valid_row(cols, prompt):
    while True:
        row = [int(x) for x in input(prompt).split()]
        if len(row) == cols:
            return row
        print(f"Error: Expected exactly {cols} elements, but got {len(row)}. Please try again.")


def input_matrix(name="Matrix"):
    print(f"--- Enter details for {name} ---")
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    matrix = []
    for i in range(rows):
        row = get_valid_row(cols, f"Enter {cols} space-separated elements for row {i}: ")
        matrix.append(row)
    print(f"\nFull 2D Form of {name}:")
    display_full_matrix(matrix)
    return matrix


def to_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    sparse = []
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != 0:
                sparse.append([r, c, matrix[r][c]])
                
    sparse.insert(0, [rows, cols, len(sparse)])
    return sparse


def to_full_matrix(sparse):
    rows, cols, _ = sparse[0]
   
    full_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for r, c, val in sparse[1:]:
        full_matrix[r][c] = val
        
    return full_matrix


def add_sparse_matrices(sparse1):
    print("--- Enter Second Matrix for Sparse Addition ---")
    matrix2 = input_matrix("Matrix 2")
    sparse2 = to_sparse(matrix2)
    
    print("Sparse Representation of Matrix 2:")
    display_sparse_matrix(sparse2)
    
    if sparse1[0][0] != sparse2[0][0] or sparse1[0][1] != sparse2[0][1]:
        print("Error: Matrix dimensions do not match! Addition is not possible.")
        return None
        
    rows, cols = sparse1[0][0], sparse1[0][1]
    result_entries = []
    
    i, j = 1, 1
    len1, len2 = len(sparse1), len(sparse2)
    
    while i < len1 and j < len2:
        r1, c1, v1 = sparse1[i]
        r2, c2, v2 = sparse2[j]
        
        if (r1, c1) < (r2, c2):
            result_entries.append([r1, c1, v1])
            i += 1
        elif (r1, c1) > (r2, c2):
            result_entries.append([r2, c2, v2])
            j += 1
        else:
            added_val = v1 + v2
            if added_val != 0: 
                result_entries.append([r1, c1, added_val])
            i += 1
            j += 1
            
    while i < len1:
        result_entries.append(sparse1[i])
        i += 1
    while j < len2:
        result_entries.append(sparse2[j])
        j += 1
        
    result_sparse = [[rows, cols, len(result_entries)]] + result_entries
    return result_sparse



matrix1 = input_matrix("Matrix 1")
sparse1 = to_sparse(matrix1)
print("Sparse Triple Representation of Matrix 1:")
display_sparse_matrix(sparse1)

reconstructed1 = to_full_matrix(sparse1)
print("Reconstructed Full 2D Form of Matrix 1 (from Sparse):")
display_full_matrix(reconstructed1)

sum_sparse = add_sparse_matrices(sparse1)

if sum_sparse is not None:
    print("Result of Addition (Sparse Triple Form):")
    display_sparse_matrix(sum_sparse)
    
    sum_full = to_full_matrix(sum_sparse)
    print("Result of Addition (Reconstructed Full 2D Form):")
    display_full_matrix(sum_full)
