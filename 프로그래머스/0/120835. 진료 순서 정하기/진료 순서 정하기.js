function solution(emergency) {
    
    var answer = [];
    emergency_copy = [...emergency];
    emergency.sort((a,b)=>b-a);
    emergency_copy.forEach((e)=>answer.push(emergency.indexOf(e)+1))
  
    return answer;
}