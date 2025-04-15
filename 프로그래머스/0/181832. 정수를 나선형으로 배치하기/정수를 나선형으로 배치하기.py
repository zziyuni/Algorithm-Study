def solution(n):
    answer = [[0] * n for _ in range(n)]
    cnt = 1
    left = 0
    right =n-1
    up = 0
    down = n-1
    direction = 0
    while cnt <= n*n:
        if direction == 0:
            for j in range(left,right+1):
                answer[up][j] = cnt
                cnt += 1
            
            up += 1
        elif direction == 1:
            for j in range(up,down+1):
                answer[j][right] = cnt
                cnt += 1
            right -=1
        elif direction == 2:
            for j in range(right,left-1,-1):
                answer[down][j] = cnt
                cnt += 1
            down -= 1
        elif direction == 3:
            for j in range(down,up-1,-1):
                answer[j][left] = cnt
                cnt +=1
            left +=1
        direction = (direction +1) % 4
         
    return answer