def solution(maps):
    answer = []
    island = []
    for m in maps:
        island.append(list(m))
        

    r = len(island)
    c = len(island[0])
    visited = [[False] * c for _ in range(r)]
    
    def dfs(a,b):
        days = 0
        stack = [(a,b)]
        while stack:
            x,y = stack.pop()
            if visited[x][y]:
                 continue
            days += int(island[x][y])
            visited[x][y] = True
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx = x + dx
                ny = y + dy
                if nx<0 or nx >=r or ny < 0 or ny >=c:
                    continue
                if island[nx][ny] != 'X':
                    stack.append((nx,ny))
        return days
                    
    
    for i in range(r):
        for j in range(c):
            if not visited[i][j] and island[i][j] !='X':
                answer.append(dfs(i,j))
    answer.sort() 
    if len(answer) == 0:
        answer.append(-1)
    return answer