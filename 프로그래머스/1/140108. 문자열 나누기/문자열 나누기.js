function solution(s) {
    s = s.split('');
    var start = s[0]
    var same = 0;
    var diff = 0;
    var answer = 0;
  
    s.forEach((e)=>{
        if(same == diff){
            answer +=1;
            start = e;
            same = 0;
            diff = 0;  
            }
        if(e === start){
            same +=1;
            }
        else{
            diff+=1;
            }
        }
             );
        
    return answer;
    
}