import sys

input = sys.stdin.readline

N = int(input())
d = list(map(int, input().split()))

max_cnt = max(d)
other_sum = sum(d) - max_cnt

if sum(d) == 1 or other_sum >= max_cnt:
    print('Happy')
else:
    print('Unhappy')
