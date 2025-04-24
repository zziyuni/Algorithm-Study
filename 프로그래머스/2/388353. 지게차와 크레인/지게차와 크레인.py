outer = []

def make_outer(outer,st,x,y):
    stack = [(x,y)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while stack:
        x,y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx <0 or nx >= len(st) or ny <0 or ny >= len(st[0]):
                continue
            if st[nx][ny] == '-1' and not outer[nx][ny]:
                stack.append((nx,ny))
            outer[nx][ny] = True
        
        
    
              
    
def 지게차(st,outer,c):
    removed = set()
    for i in range(len(st)):
        for j in range(len(st[0])):
            if st[i][j] == c:
                if outer[i][j]:
                    st[i][j] = '-1'
                    removed.add((i,j))
    for r in removed:
        x,y = r
        make_outer(outer,st,x,y)

            
def 크레인(st,outer,c):
    for i in range(len(st)):
        for j in range(len(st[0])):
            if st[i][j] == c:
                st[i][j] = '-1'
                if outer[i][j]:
                    make_outer(outer,st,i,j)
                
                
                

def solution(storage, requests):
    answer = 0
    outer = [[False] * len(storage[0]) for _ in range(len(storage))]
    new_storage = []
    for i in range(len(storage)):
        outer[i][0] = True
        outer[i][-1] = True
    for i in range(len(storage[0])):
        outer[0][i] = True
        outer[-1][i] = True
    
    
    for s in storage:
        new_storage.append(list(s))
        
    for r in requests:
        if len(r) == 2:
            크레인(new_storage,outer,r[0])
        else:
            지게차(new_storage,outer,r)
        
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if new_storage[i][j] != '-1':
                answer+=1
    

    return answer
