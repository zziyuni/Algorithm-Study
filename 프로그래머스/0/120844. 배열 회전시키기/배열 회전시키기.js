function solution(numbers, direction) {
    if(direction ==='right'){
    numbers.unshift( numbers.pop())
       
    }
    if(direction ==='left'){
        numbers.push(numbers.shift())
    }
   
    return numbers;
}