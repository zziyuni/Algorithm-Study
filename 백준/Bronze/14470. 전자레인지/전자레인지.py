A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

ans = 0
if A < 0:
    ans += C * abs(A) + D
    A = 0
ans += (B-A) * E

print(ans)
