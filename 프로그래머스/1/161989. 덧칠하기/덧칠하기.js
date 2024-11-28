function solution(n, m, section) {
    var cur = section[0]-1
    var answer = 1;
    for(let i = 1;i<section.length;i++){
        if(section[i]-cur > m){
            cur = section[i]-1
            answer+=1
        }
    }
    return answer;
}