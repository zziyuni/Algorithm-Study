function solution(polynomial) {
    terms = polynomial.split(' + ');
    let x = 0
    let num = 0
    terms.forEach((e)=>{
        if(e == 'x') x+=1
       else if(e.includes('x')) x += Number(e.slice(0,-1).toString())
        else num+= Number(e) })
    let x_term = x > 0 ? x == 1 ?'x':`${x}x`:'';
    let num_term =  num >0 ?x >0?` + ${num}`:`${num}`: ''
    var answer = `${x_term}${num_term}`;
    return answer;
}