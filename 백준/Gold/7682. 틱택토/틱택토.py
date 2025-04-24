import sys

input = sys.stdin.readline


def check_end(tc):
    cnt_x = tc.count('X')
    cnt_o = tc.count('O')
    if not (cnt_x == cnt_o or cnt_x - 1 == cnt_o):
        return False
    c = 0
    r = 0
    diag = 0
    win_O = False
    win_X = False

    for i in range(3):
        pre = ''
        flag = True
        for j in range(i, 9, 3):
            if tc[j] == '.':
                flag = False
                break
            if pre == '':
                pre = tc[j]
            else:
                if pre != tc[j]:
                    flag = False
                    break
                pre = tc[j]
        if flag:
            c += 1
            if pre == 'O':
                if win_X:
                    return False
                else:
                    win_O = True
            else:
                if win_O:
                    return False
                else:
                    win_X = True

    if tc[0] == tc[4] == tc[8]:
        if tc[0] != '.':
            if tc[0] == 'O':
                win_O = True
            else:
                win_X = True
            diag += 1

    if tc[2] == tc[4] == tc[6]:
        if tc[2] != '.':
            if tc[2] == 'O':
                win_O = True
            else:
                win_X = True
            diag += 1
    for i in range(0, 9, 3):
        pre = ''
        flag = True
        for j in range(3):
            if tc[i + j] == '.':
                flag = False
                break
            if pre == '':
                pre = tc[i + j]
            else:
                if pre != tc[i + j]:
                    flag = False
                    break
                pre = tc[i + j]
        if flag:
            r += 1
            if pre == 'O':
                if win_X:
                    return False
                else:
                    win_O = True
            else:
                if win_O:
                    return False
                else:
                    win_X = True

    if win_O:
        if cnt_x > cnt_o:
            return False
    else:
        if cnt_x == cnt_o:
            return False
    if t.count('.') == 0 and diag == 0 and r == 0 and c == 0:
        return True

    if r > 1 or c > 1:
        return False
    if diag == 1:
        if r == 1 and c == 1:
            return False
        return True
    if diag == 2:
        if r == 0 and c == 0:
            return True
        return False
    if diag == 0:
        if r == 0 and c == 0:
            return False
        return True




while True:
    t = input().strip()
    if t == 'end':
        break
    if check_end(list(t)):
        print('valid')
    else:
        print('invalid')
