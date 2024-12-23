import sys

input = sys.stdin.readline

N, L = map(int, input().split())
traffic_info = list(list(map(int, input().split())) for _ in range(N))

current_time = 0
pre_pos = 0
for info in traffic_info:
    D, R, G = info
    current_time += D - pre_pos
    if current_time % (R + G) < R:
        current_time += R - current_time % (R + G)
    pre_pos = D

current_time += L - pre_pos
print(current_time)
