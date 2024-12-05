function solution(numbers) {
    var answer = [];
   for(let i = 0;i<numbers.length;i++){
       for(let j = i+1; j<numbers.length;j++){
           answer.push(numbers[i]+numbers[j]);
           
       }
   }
    const set = new Set(answer);
    answer = [...set]
    
    return answer.sort((a,b)=>a-b);
}