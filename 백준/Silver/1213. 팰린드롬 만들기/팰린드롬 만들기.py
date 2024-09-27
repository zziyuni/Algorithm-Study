name = input()

alpha = [0] * 26

ans = ''
mid = ''
for c in name:
    alpha[ord(c) - ord('A')] += 1

for i in range(26):
    if alpha[i] == 0:
        continue
    if alpha[i] % 2 == 0:
        ans += (chr(i + 65) * (alpha[i] // 2))
    else:
        if mid != '':
            print("I'm Sorry Hansoo")
            exit()

        else:
            ans += (chr(i + 65) * (alpha[i] // 2))
            mid = chr(i + 65)

print(ans + mid + ans[::-1])
