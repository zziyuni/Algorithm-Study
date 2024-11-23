function solution(box, n) {
    var answer = 1;
    box.forEach((e)=>answer*=Math.floor(e/n))
    return answer;
}