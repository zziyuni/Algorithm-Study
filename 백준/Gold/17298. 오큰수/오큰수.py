import sys

input = sys.stdin.readline

N = int(input())
NGE = [-1] * N
stack = [0]
nums = list(map(int, input().split()))

for i in range(N):
    while stack and nums[i] > nums[stack[-1]]:
        NGE[stack.pop()] = nums[i]
    stack.append(i)

print(*NGE)
