e, s, m = map(int, input().split())

i = 1
while True:
    if ((i % 15 == 0 and e == 15) or i % 15 == e) and ((i % 28 == 0 and s == 28) or i % 28 == s) and (
            (i % 19 == 0 and m == 19) or i % 19 == m):
        break

    i += 1

print(i)
