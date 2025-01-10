N, m, M, T, R = map(int, input().split())

answer = N
pulse = m

if m + T > M:
    print(-1)
else:
    for _ in range(N):
        if pulse + T > M:
            while pulse + T > M:
                pulse -= R
                answer += 1
        pulse = max(m, pulse)
        pulse += T
    print(answer)
