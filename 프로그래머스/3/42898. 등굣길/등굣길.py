
def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    puddle_set = set((y - 1, x - 1) for x, y in puddles)
    
    for i in range(m):
        if (0,i) in puddle_set:
            break
        
        dp[0][i] = 1
    for i in range(n):
        if (i,0) in puddle_set:
            break
        
        dp[i][0] = 1
        
    for i in range(1,n):
        for j in range(1,m):
            if (i,j) in puddle_set:
                continue
                
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
    
        
    return dp[n-1][m-1] % 1000000007