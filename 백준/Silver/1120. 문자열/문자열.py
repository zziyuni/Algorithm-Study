a, b = input().split()

if len(a) == len(b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
else:
    cnt = 51
    for j in range(len(b) - len(a) + 1):
        tmp = 0
        for i in range(len(a)):
            if a[i] != b[i + j]:
                tmp += 1

        cnt = min(cnt, tmp)

print(cnt)
