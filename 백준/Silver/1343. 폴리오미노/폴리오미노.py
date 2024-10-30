board = input().strip()

poly = board.split('.')

poly = list(filter(lambda x: x != '', poly))


def check_cover(p):
    if len(p) % 4 == 0:
        return 'AAAA' * (len(p) // 4)
    elif len(p) % 2 == 0:
        return 'AAAA' * (len(p) // 4) + 'BB' * (len(p) % 4 // 2)
    return False


pos = 0
i = 0
ans = ''
while i < len(board):
    if board[i] != '.':
        if not check_cover(poly[pos]):
            ans = -1
            break
        ans += check_cover(poly[pos])
        i += len(poly[pos])
        pos += 1
    else:
        ans += '.'
        i += 1
print(ans)
