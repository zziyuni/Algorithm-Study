import sys

input = sys.stdin.readline

s = input().strip()

n = int(input())
cnt = 0
for _ in range(n):
    st = input().strip()
    if s in st*2:
        cnt += 1

print(cnt)
