from collections import deque

def solution(board):
    answer = -1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    def bfs(a,b):
        queue = deque([[a,b,0]])
        
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        visited[a][b] = True
        while queue:
            x,y,time = queue.popleft()
            if board[x][y] == 'G':
                return time
            for i in range(4):
                nx = x
                ny = y
                
                while True:
                    nx +=dx[i]
                    ny +=dy[i]
                    if nx <0 or ny < 0 or nx >=len(board) or ny >= len(board[0]):
                        nx -=dx[i]
                        ny -=dy[i]
                        break
                    if board[nx][ny] == 'D':
                        nx -=dx[i]
                        ny -=dy[i]
                        break
                    
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                queue.append([nx,ny,time+1])
        return -1
              
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                answer = bfs(i,j)
    return answer