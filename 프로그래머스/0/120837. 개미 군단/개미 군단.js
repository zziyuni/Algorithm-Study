function solution(hp) {
    var answer = 0;
    answer += Math.floor(hp/5);
    hp -= 5 * Math.floor(hp/5);
    
    if(hp > 0) {
        answer += Math.floor(hp/3);
        hp -=  3 * Math.floor(hp/3);     
    }
    if(hp > 0) answer += hp;
    
    return answer;
}