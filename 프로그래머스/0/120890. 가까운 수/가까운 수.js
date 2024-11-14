function solution(array, n) {
    array.sort()
    diff =  array.map((e) => Math.abs(e-n))
    return array[diff.indexOf(Math.min(...diff))]
}