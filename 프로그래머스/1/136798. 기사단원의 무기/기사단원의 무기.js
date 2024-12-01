function solution(number, limit, power) {
    var attack= Array(number+1).fill(0);
    for(let i = 1;i<number+1;i++){
        var cnt = 0;
        for(let j = 1;j<=Math.sqrt(i);j++){
            if(i%j == 0){
                cnt+=1;
                if(i/j != j){
                    cnt+=1
                }
            }
            
        }
        attack[i] = cnt;
    }
    
    attack = attack.map((e)=>{
        if(e > limit){
         return e = power;
        }
        return e
    })
    
    return attack.reduce((acc,cur)=>acc+cur, 0);
}