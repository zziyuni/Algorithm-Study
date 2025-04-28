def solution(record):
    answer = []
    id_map = {}
    for r in record:
        t = r.split()[0]
        if t == 'Leave':
            continue
        t,uid,name =r.split()
        id_map[uid] = name
    for r in record:
        t = r.split()[0]
        uid = r.split()[1]
        if t == 'Enter':
            answer.append(id_map[uid] +'님이 들어왔습니다.')
        elif t =='Leave':
            answer.append(id_map[uid]+'님이 나갔습니다.')
            
    
    return answer