def solution(routes):
    answer = 1
    
    routes.sort(key=lambda x:(x[1]))
    install = routes[0][1]
    for i in range(1,len(routes)):
        if install <routes[i][0]:
            answer+=1
            install = routes[i][1]
        
    return answer