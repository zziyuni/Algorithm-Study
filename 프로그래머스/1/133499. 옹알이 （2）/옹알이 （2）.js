function check(word){
    const patterns = ["aya", "ye", "woo", "ma"];
    var pre = '';
    while(word !==""){
        var flag = true;
    for (const pattern of patterns) {
        if(word.slice(0,pattern.length) === pattern && pattern !== pre){
            word = word.slice(pattern.length,);
            flag = false;
            pre = pattern;
        }
    }
        if(flag){
            return false;
        }
    }
    return true;
}

function solution(babbling) {
    var answer = 0;
    babbling.forEach((e)=>{
        if(check(e)){
            answer+=1;
        }
    })
    return answer;
}