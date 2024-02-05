import sys

input = sys.stdin.readline
n, m = map(int, input().split())

words = {}
for _ in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1


sorted_words = dict(sorted(words.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))

for key in sorted_words.keys():
    print(key)