function solution(score) {
    var answer = [];
    score = score.map((e)=>(e[0]+e[1])/2)
    let ranking = score.slice().sort((a,b)=>b-a)
    score.forEach((e)=>answer.push(ranking.indexOf(e)+1))
    return answer;
}