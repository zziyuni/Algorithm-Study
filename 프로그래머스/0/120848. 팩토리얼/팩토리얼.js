

function solution(n) {
    var k = 1;
    var i = 1;
    while(true){
        k*=i
        if(k > n){
            break
        }
        i+=1
        
    }
    
    return i-1;
}