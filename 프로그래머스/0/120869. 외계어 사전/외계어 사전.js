function solution(spell, dic) {
    if (dic.some((e)=>(e.length == spell.length) && spell.every((e2)=>e.includes(e2))))
        return 1
    return 2
}