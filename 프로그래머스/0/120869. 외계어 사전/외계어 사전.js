function solution(spell, dic) {
    if (dic.some((e)=>spell.every((e2)=>e.includes(e2))))
        return 1
    return 2
}