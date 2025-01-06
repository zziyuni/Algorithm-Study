import sys

input = sys.stdin.readline

N, K = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

start = 0
end = N - 1
answer = 0
while start < end:
    if weights[start] + weights[end] <= K:
        start += 1
        end -= 1
        answer += 1
    else:
        end -= 1

print(answer)
