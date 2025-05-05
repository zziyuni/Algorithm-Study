def solution(triangle):
    answer = 0
    t_len = len(triangle)
    dp = [[0] * t_len for _ in range(t_len)]
    dp[0][0] = triangle[0][0]
    for i in range(1,t_len):
        for j in range(i+1):
            if j-1 <0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            else:
                dp[i][j] = max(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1])

            
    return max(dp[t_len-1])