board = input().strip()

cnt = 0
ans = ''
for b in board:
    if b == 'X':
        cnt += 1
        if cnt == 4:
            ans += 'AAAA'
            cnt = 0
    else:
        if cnt == 2:
            ans += 'BB'
        elif cnt != 0:
            ans = -1
            break
        ans += '.'
        cnt = 0

if cnt == 2:
    ans += 'BB'
    cnt = 0
if cnt != 0:
    ans = -1
print(ans)
