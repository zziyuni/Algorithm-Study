def dfs(a, b, c, back1, back2):
    global ans, have_alpha

    if a == have_alpha[0] and b == have_alpha[1] and c == have_alpha[2]:
        return True
    if dp[a][b][c][back1][back2]:
        return False
    dp[a][b][c][back1][back2] = True

    if a + 1 <= have_alpha[0]:
        ans[a + b + c] = 'A'
        if dfs(a + 1, b, c, back2, 0):
            return True

    if b + 1 <= have_alpha[1]:
        ans[a + b + c] = 'B'
        if back2 != 1:
            if dfs(a, b + 1, c, back2, 1):
                return True

    if c + 1 <= have_alpha[2]:
        ans[a + b + c] = 'C'
        if back1 != 2 and back2 != 2:
            if dfs(a, b, c + 1, back2, 2):
                return True

    return False


s = input()
have_alpha = [0, 0, 0]
for char in s:
    if char == 'A':
        have_alpha[0] += 1
    elif char == 'B':
        have_alpha[1] += 1
    else:
        have_alpha[2] += 1

dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
ans = ['' for _ in range(len(s))]

if dfs(0, 0, 0, -1, -1):
    for char in ans:
        print(char, end='')
else:
    print(-1)
