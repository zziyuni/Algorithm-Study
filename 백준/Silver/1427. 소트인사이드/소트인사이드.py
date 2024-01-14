number = input()

arr = [int(num) for num in number]

arr.sort(reverse=True)
for i in arr:
    print(i, end='')
