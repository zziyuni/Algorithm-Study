def solution(money):
    answer = 0
    n = len(money)
    dp = [0] * n
    dp2 = [0] * n
    for i in range(n):
        dp[i] = money[i]
        dp2[i] = money[i]
    dp2[0] = 0
    
    for i in range(2,n):
        dp[i] = max(dp[i-2]+money[i], dp[i-1] - money[i-1] + money[i])
        dp2[i] = max(dp2[i-2]+money[i], dp2[i-1] - money[i-1] + money[i])
    
    dp[n-1] = dp2[n-1]
    
        
    answer = max(dp)
        
        
    return answer