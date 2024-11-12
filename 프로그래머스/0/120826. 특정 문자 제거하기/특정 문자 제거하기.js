function solution(my_string, letter) {
   
    return Array.from(my_string).filter((e)=>e!=letter).join('');
}