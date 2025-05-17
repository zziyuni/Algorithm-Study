def solution(n, wires):
    answer = 1e9
    nodes = [[] for _ in range(n+1)]
    for a,b in wires:
        nodes[a].append(b)
        nodes[b].append(a)
    def dfs(a,b):
        stack = [a]
        cnt = 0
        visited = [False] * (n+1)
        visited[b] = True
        while stack:
            cur = stack.pop()
            visited[cur] = True
            cnt +=1
            for neighbor in nodes[cur]:
                if not visited[neighbor]:
                    stack.append(neighbor)
        return cnt
                
            
    for w in wires:
        first = dfs(w[0],w[1])
        second = n - first
        answer = min(abs(first-second),answer)
        
    return answer