function solution(s) {
    let map = new Map()
    let answer = '';
    s = s.split('')
    console.log(s)
    s.forEach((e)=>{
              if(map.has(e))
                  map.set(e, map.get(e)+1)
    else map.set(e,1)})
    console.log(map)
   Array.from(map.keys()).forEach((e)=>{if(map.get(e) == 1){
        answer+=e
    }})
    answer = answer.split('').sort().join('')
    return answer
}