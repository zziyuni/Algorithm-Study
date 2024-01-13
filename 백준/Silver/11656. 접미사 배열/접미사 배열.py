sentence = input().strip()

arr = []
for i in range(len(sentence)):
    arr.append(sentence[i:len(sentence)])
arr = sorted(arr)
for suffix in arr:
    print(suffix)
