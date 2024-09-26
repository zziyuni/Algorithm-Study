

def backtracking(n,row,columns,diag_up,diag_down):
    if row == n:
        return 1
    answers = 0
    for col in range(n):
        if not columns[col] and not diag_up[col+row] and not diag_down[col-row +(n-1)]:
            columns[col] = True
            diag_up[col+row] = True
            diag_down[col-row +(n-1)] = True
            answers += backtracking(n,row+1,columns,diag_up,diag_down)
            columns[col] = False
            diag_up[col+row] = False
            diag_down[col-row +(n-1)] = False
                
    return answers
    

def solution(n):
    columns = [False] * n
    diag_up = [False] * (2 * n - 1) # 상향 대각선 체크
    diag_down = [False] * (2 * n - 1) # 하향 대각선 체크
    
    return backtracking(n,0,columns,diag_up,diag_down)

