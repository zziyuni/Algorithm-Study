function solution(balls, share) {
    var answer = 1;
    for(let i = balls;i>balls-share;i--){
        answer *= i;
        
    }
    for(let i=1;i<=share;i++){
       answer=Math.round(answer/i);
    }
    return answer;
}