function solution(cards1, cards2, goal) {
    let one_cur = 0;
    let two_cur = 0;

    for (let i = 0; i < goal.length; i++) {
        if (goal[i] === cards1[one_cur]) {
            one_cur += 1;
        } else if (goal[i] === cards2[two_cur]) {
            two_cur += 1;
        } else {
            return "No"; 
        }
    }

    return "Yes"; 
}