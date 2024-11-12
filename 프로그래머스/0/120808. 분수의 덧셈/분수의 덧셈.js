function solution(numer1, denom1, numer2, denom2) {
    var numer = numer1*denom2 + numer2*denom1;
    var denom = denom1*denom2;
    const min_val = Math.min(numer,denom)
    for(let i = min_val;i>1;i--){
        if (numer %i === 0 && denom %i === 0){
            numer /= i;
            denom /= i;
        }
        
    }
    
    var answer = [numer,denom];
    return answer;
}