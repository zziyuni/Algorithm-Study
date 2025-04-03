def solution(info, n, m):
    item_cnt = len(info)
    dp = [[1e9] * m for _ in range(item_cnt + 1)]
    dp[0][0] = 0
    
    for i in range(item_cnt):
        a,b = info[i]
        for j in range(m):
            if dp[i][j] + a < n:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+a)
            if j + b < m:
                dp[i+1][j+b] = min(dp[i+1][j+b],dp[i][j])
    answer = min(dp[item_cnt]) 
    return answer if answer != 1e9 else -1