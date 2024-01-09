import sys

input = sys.stdin.readline

num_list = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
            "8": "eight", "9": "nine"}
m, n = map(int, input().split())

arr = []
for i in range(m, n + 1):
    temp = ''
    for j in str(i):
        temp += num_list[j]
    arr.append([i, temp])

sorted_list = sorted(arr, key=lambda x: list(x)[1])

for i in range(len(sorted_list)):

    if i % 10 == 0 and i != 0:
        print()
    print(sorted_list[i][0], end=' ')
