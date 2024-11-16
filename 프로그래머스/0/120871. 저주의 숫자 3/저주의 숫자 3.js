function solution(n) {
    ans = 0

    for(let i =1; i <=n;i++){
        ans +=1
        while(ans%3 == 0 || ans.toString().includes('3')){
            ans+=1
        }
        
    }
    return ans
    
}