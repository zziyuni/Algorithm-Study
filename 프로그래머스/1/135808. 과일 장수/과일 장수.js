function solution(k, m, score) {
    var box = [];
    var answer = 0;
    const remain = score.length%m
    score.sort((a,b)=>a-b)
    score = score.slice(remain,)
    for(let i = 0;i<score.length;i+=m){
        answer+=score[i]*m;
    }
    return answer;
}