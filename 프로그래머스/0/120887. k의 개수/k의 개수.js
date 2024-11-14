function solution(i, j, k) {
    let answer = 0;
    for(i;i<=j;i+=1){
        array = i.toString().split('');
        array.forEach((e)=>{if(e==k) answer+=1})
    }
    return answer;
}