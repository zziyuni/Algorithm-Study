import sys

input = sys.stdin.readline

N = int(input())

words = list(input().strip() for _ in range(N))

words.sort(key=lambda x: -len(x))

group = [[] for _ in range(N)]

flag = True
for i in range(N):
    word = words[i]
    for j in range(N):
        for k in group[j]:
            if k[:len(word)] == word:
                flag = False
                break
        if flag:
            group[j].append(word)
            break
        flag = True

ans = 0
for i in range(N):
    if len(group[i]) == 0:
        break
    ans = max(len(group[i]), ans)

print(ans)