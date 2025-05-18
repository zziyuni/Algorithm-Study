import heapq
def solution(n, costs):
    answer = 0
    edges = [[] for _ in range(n)]
    for c in costs:
        a,b,cost =c
        edges[a].append((b,cost))
        edges[b].append((a,cost))
    
    nodes = [(0,0)]
    visited = set()
    while nodes:
        c,cur = heapq.heappop(nodes)
        if cur in visited:
            continue
        visited.add(cur)
        answer += c
        
        for neighbor,cost in edges[cur]:
            if neighbor not in visited:
                heapq.heappush(nodes,(cost,neighbor))
                
            
        
    return answer