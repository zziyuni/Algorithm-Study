import sys
from itertools import accumulate

input = sys.stdin.readline

n = int(input())

time = list(map(int,input().split()))

sorted_time = sorted(time)

sum_time = list(accumulate(sorted_time))

print(sum(sum_time))