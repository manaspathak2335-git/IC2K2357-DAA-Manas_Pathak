# Program to initialize a 2D array from user input and sequentially perform row insertion, 
# row deletion, 2D element search, and a 90-degree clockwise matrix rotation.

def display_matrix(matrix):
    if not matrix:
        print("Matrix is empty.\n")
        return
    for row in matrix:
        print(row)
    print()


def get_valid_row(cols, prompt):
    while True:
        row = [int(x) for x in input(prompt).split()]
        if len(row) == cols:
            return row
        print(f"Error: Expected exactly {cols} elements, but got {len(row)}. Please try again.")


def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row = get_valid_row(cols, f"Enter {cols} space-separated elements for row {i}: ")
        matrix.append(row)
    print("\nInitial 2D Array:")
    display_matrix(matrix)
    return matrix, cols


def insert_row(matrix, cols):
    pos = int(input("Enter row position (index) to insert at: "))
    
    if 0 <= pos <= len(matrix):
        new_row = get_valid_row(cols, f"Enter {cols} space-separated elements for the new row: ")
        matrix.insert(pos, new_row)
        print(f"\n2D Array after inserting row at index {pos}:")
    else:
        print("\nInvalid row position for insertion.")
    display_matrix(matrix)


def delete_row(matrix):
    pos = int(input("Enter row position (index) to delete: "))
    
    if 0 <= pos < len(matrix):
        matrix.pop(pos)
        print(f"\n2D Array after deleting row at index {pos}:")
    else:
        print("\nInvalid row position for deletion.")
    display_matrix(matrix)


def search_element(matrix):
    target = int(input("Enter value to search in the 2D array: "))
    found = False
    
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == target:
                print(f"\nValue {target} found at Row {r}, Column {c}.")
                found = True
                break
        if found:
            break
            
    if not found:
        print(f"\nValue {target} not found in the 2D array.")
        
    print("Current 2D Array:")
    display_matrix(matrix)


def rotate_90_clockwise(matrix):
    if not matrix or not matrix[0]:
        print("Cannot rotate an empty matrix.")
        return

    rows = len(matrix)
    cols = len(matrix[0])
    
    rotated = []
    for c in range(cols):
        new_row = []
        for r in range(rows - 1, -1, -1):
            new_row.append(matrix[r][c])
        rotated.append(new_row)
        
    matrix[:] = rotated  
    print("2D Array after rotating 90 degrees clockwise:")
    display_matrix(matrix)



matrix, cols = input_matrix()
insert_row(matrix, cols)
delete_row(matrix)
search_element(matrix)
rotate_90_clockwise(matrix)
