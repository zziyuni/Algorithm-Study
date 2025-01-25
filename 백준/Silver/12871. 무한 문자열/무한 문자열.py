s = input().strip()
t = input().strip()

s_length = len(s)
t_length = len(t)

lcm = 0
for i in range(max(s_length, t_length), s_length * t_length + 1):
    if i % s_length == 0 and i % t_length == 0:
        lcm = i
        break

if s * (lcm // s_length) == t * (lcm // t_length):
    print(1)
else:
    print(0)