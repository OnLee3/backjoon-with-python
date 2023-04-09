function solution(clothes) {
    const combination = {};
    const clothesLength = [];
    
    for (let i = 0; i < clothes.length; i ++) {
        if (combination.hasOwnProperty(clothes[i][1])) {
            combination[clothes[i][1]].push(clothes[i][0]);
        } else {
            combination[clothes[i][1]] = [clothes[i][0]];   
        }
    }
    for (const [key, value] of Object.entries(combination)) {
        clothesLength.push(value.length + 1);
    }

    return clothesLength.reduce((a, b) => a * b, 1) - 1;
}