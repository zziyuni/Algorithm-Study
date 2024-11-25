function solution(name, yearning, photo) {
    return photo.map(arr =>
        arr.reduce((acc, cur) => {
            const index = name.indexOf(cur);
            return acc + (index !== -1 ? yearning[index] : 0);
        }, 0)
    );
}