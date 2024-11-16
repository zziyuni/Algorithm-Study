function solution(s) {
    nums = s.split(' ')
    stack = []
    nums.forEach((e)=>{
    if (e == 'Z') stack.pop()
    else stack.push(Number(e))
                 })
    
    return stack.reduce((acc,cur)=>acc+cur,0)
}