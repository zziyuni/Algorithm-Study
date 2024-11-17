function solution(my_string, n) {
    var answer = '';
    my_string.split('').forEach((e)=>answer+=e.repeat(n))
    return answer;
}