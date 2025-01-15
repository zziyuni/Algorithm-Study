import sys

input = sys.stdin.readline

N = int(input())
history = list(list(map(int, input().split())) for _ in range(N))
person = [1] * 200001
ans = 0
for i in range(N):
    a, b = history[i]
    if person[a] != b:
        ans += 1
    person[a] = abs(b - 1)

ans += person.count(0)

print(ans)