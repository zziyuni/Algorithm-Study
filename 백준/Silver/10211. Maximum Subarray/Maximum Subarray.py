import sys

input = sys.stdin.readline

T = int(input())


def get_prefix_sum(a):
    prefix = [0] * len(a)
    prefix[0] = a[0]
    for i in range(1, len(a)):
        prefix[i] = prefix[i - 1] + a[i]
    return prefix


def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(max_subarray_sum(arr))
