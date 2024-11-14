function solution(array) {
    cntArray = Array(1000).fill(0)
    array.forEach((e)=>cntArray[e]+=1)
    let count = cntArray.filter(element => Math.max(...cntArray) === element).length;
    if(count>1) return -1
    return cntArray.indexOf(Math.max(...cntArray))
    
}