def is_safe(row,col,Q):
    for i in range(row):
        if Q[i]==col or abs(Q[i]-col) == abs(row-i):
            return False
    return True

def solve_8_queens(Q,row):
    if row==8:
        print(Q)
        return
    for i in range(8):
        if is_safe(row,i,Q):
            Q[row]=i
            solve_8_queens(Q,row+1)

Q=[-1]*8
solution=solve_8_queens(Q,0)
    
