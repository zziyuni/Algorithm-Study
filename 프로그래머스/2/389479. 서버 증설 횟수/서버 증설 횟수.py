def solution(players, m, k):
    answer = 0
    cur_server = []
    for p in players:
        cnt_server = 0
        for i in range(len(cur_server)):
            cnt, time = cur_server[i]
            if time+1 <= k:
                cur_server[i] = [cnt,time+1]
                cnt_server += cnt 
        if p >= m and cnt_server < p//m:
            answer += p//m -cnt_server 
            cur_server.append([p//m -cnt_server,1])
        
    return answer


#m명 마다 서버 +1
#m명 미만 그대로
#서버 k 시간 운영하고 반납

#서버 몇번 증설해야하나?