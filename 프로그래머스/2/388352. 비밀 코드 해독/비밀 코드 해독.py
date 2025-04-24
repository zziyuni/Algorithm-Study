from itertools import combinations
import copy

answer = 0
def find_secret(q,c,a):
    c = set(c)
    for i in range(len(q)):
        cnt = 0
        for j in q[i]:
            if j in c:
                cnt +=1
        if cnt != a[i]:
            return False
    return True

            
            
def solution(n, q, ans):
    answer = 0
    candidates = combinations(range(1,n+1),5)
    for c in candidates:
        if find_secret(q,c,ans):
            answer +=1
    
    return answer