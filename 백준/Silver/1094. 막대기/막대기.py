X = int(input())
length = [64]


while sum(length) > X:
    new = min(length) / 2
    if sum(length) - new >= X:
        length.remove(new*2)
        length.append(new)
    else:
        length.remove(new * 2)
        length.append(new)
        length.append(new)


print(len(length))
