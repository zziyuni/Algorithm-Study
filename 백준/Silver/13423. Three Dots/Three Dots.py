import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    X = list(map(int, input().split()))
    dis_set = set(X)
    X.sort()

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            diff = 2 * X[j] - X[i]
            if diff in dis_set:
                ans += 1
    print(ans)
