function solution(A, B) {
    for(let i = 0; i <=B.length;i ++){  
        if(A.split('').slice(-i,).join('')+A.split('').slice(0,-i).join('') === B)
            return i;   
    }
    return -1;
}