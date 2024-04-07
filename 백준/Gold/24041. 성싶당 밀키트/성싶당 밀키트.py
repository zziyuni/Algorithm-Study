import sys

input = sys.stdin.readline

n, g, k = map(int, input().split())

important_ingredient = []
ingredient = []

for _ in range(n):
    s, l, o = map(int, input().split())
    if o == 0:
        important_ingredient.append((s, l))
    else:
        ingredient.append((s, l))


def calc_germ(d):
    sum_germ = 0
    for i in important_ingredient:
        sum_germ += i[0] * max(1, d - i[1])
    sorted_ingredient = sorted(ingredient, key=lambda x: -(x[0] * max(1, d - x[1])))
    for j in range(k, len(sorted_ingredient)):
        sum_germ += sorted_ingredient[j][0] * max(1, d - sorted_ingredient[j][1])
    return sum_germ


day = 0
start = 0
end = int(2e9)
while start <= end:
    mid = (start + end) // 2
    germ = calc_germ(mid)
    if germ > g:
        end = mid - 1
    else:
        day = mid
        start = mid + 1

print(day)
