function solution(t, p) {
    var answer = 0;
    t= t.split('');
    var sub = [];
    for(let i = 0;i+p.length<=t.length;i++){
        sub.push(t.slice(i,i+p.length));
    }
    sub.forEach((e)=>{
        if(parseInt(e.join('')) <= parseInt(p)){
        answer+=1;
    }})
    return answer;
}