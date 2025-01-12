import math

l = int(input())
r = int(input())
k = int(input())

if k == 2:
    print(max(0, r - max(3, l) + 1))
elif k == 3:
    print(max(0, r // 3 - max(1, math.ceil(l / 3) - 1)))
elif k == 4:
    if l <= 10 <= r < 14:
        print(1)
    else:
        if math.ceil(l / 2) == 6:
            print(max(0, r // 2 - max(5, math.ceil(l / 2))))
        else:
            print(max(0, r // 2 - max(5, math.ceil(l / 2) - 1)))
elif k == 5:
    print(max(0, r // 5 - max(2, math.ceil(l / 5) - 1)))
