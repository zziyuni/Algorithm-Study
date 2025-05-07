def solution(land):
    answer = 0
    n = len(land)
    m =len(land[0])
    visited = [[False] * m for _ in range(n)]
    oils = [set() for _ in range(m)]
    def bfs(a,b,cnt):
        stack = [(a,b)]
        path = set([b])
        a = 0
        while stack:
            x,y = stack.pop()
            oils[y].add(cnt)
            a +=1
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = x+dx
                ny = y+dy
                if nx <0 or ny < 0 or nx >=n or ny>=m:
                    continue
                if not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    path.add(ny)
                    stack.append((nx,ny))
        return a
     
    amounts = []
    cnt = 0
    for i in range(n):
        
        for j in range(m):
            if visited[i][j] or land[i][j] == 0:
                continue
            visited[i][j] =True
            a = bfs(i,j,cnt)
            cnt+=1
            amounts.append(a)
    
    for i in range(m):
        total = 0
        for idx in oils[i]:
            total+=amounts[idx]
                
        answer = max(total, answer)
                
                
                
        
            
            
            
    return answer