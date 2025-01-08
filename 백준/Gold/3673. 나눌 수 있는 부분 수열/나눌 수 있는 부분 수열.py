import sys

input = sys.stdin.readline

c = int(input())


def prefix_sum(n, arr):
    prefixSum = [0] * n
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]
    return prefixSum


for _ in range(c):
    d, n = map(int, input().split())
    answer = 0
    array = list(map(int, input().split()))
    prefix = prefix_sum(n, array)
    remainder = dict()
    remainder[0] = 1
    for i in range(n):
        if prefix[i] % d in remainder:
            answer += remainder[prefix[i] % d]
            remainder[prefix[i] % d] += 1
        else:
            remainder[prefix[i] % d] = 1

    print(answer)
