function solution(t, p) {
    var answer = 0;
    for(let i = 0;i+p.length<=t.length;i++){
        if(parseInt(t.slice(i,i+p.length)) <= parseInt(p)){
        answer+=1;
        }
    }
    return answer;
}