import heapq
def solution(N, road, K):
    
    answer = 0
    edges = [[] for _ in range(N+1)]
    for r in road:
        a,b,c = r
        edges[a].append((b,c))
        edges[b].append((a,c))
    costs = [1e9] * (N+1) 
    costs[1] = 0
    hq = [(0,1)]
    while hq:
        cost,cur = heapq.heappop(hq)
        if cost >costs[cur]:
            continue
        for neighbor,c in edges[cur]:
            if costs[neighbor] > c+cost:
                costs[neighbor] = c+cost
                heapq.heappush(hq, (costs[neighbor], neighbor))
                
        
    for i in range(1,N+1):
        if costs[i]<=K:
            answer +=1
            
    return answer