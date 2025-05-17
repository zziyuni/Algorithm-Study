def solution(n, computers):
    answer = 0
    nodes = [[] for _ in range(n)]
    visited = [False] * n
    def dfs(a):
        stack = [a]
        while stack:
            x = stack.pop()
            visited[x] = True
            for neighbor in nodes[x]:
                if not visited[neighbor]:
                    stack.append(neighbor)
            
            
            
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                nodes[i].append(j)
                nodes[j].append(i)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
                
    return answer