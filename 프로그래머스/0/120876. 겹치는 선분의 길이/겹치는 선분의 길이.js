function solution(lines) {
    var answer = 0;
    let arr = Array(201).fill(0)
    lines.forEach((e)=>{
        for(let i = e[0]+1;i<=e[1];i++)
                  if(arr[i+100] === 0){
                      arr[i+100] = 1
                  }else if(arr[i+100] === 1){
                      answer +=1
                      arr[i+100] = 2
                  }
                  }
                 )

    
    return answer
}