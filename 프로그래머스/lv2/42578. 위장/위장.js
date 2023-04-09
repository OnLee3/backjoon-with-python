function solution(clothes) {
    const clothingCounts = new Map();

    for (const [name, type] of clothes) {
        clothingCounts.set(type, (clothingCounts.get(type) || 0) + 1);
    }

    let combinations = 1;
    for (const count of clothingCounts.values()) {
        combinations *= (count + 1);
    }

    return combinations - 1;
}
