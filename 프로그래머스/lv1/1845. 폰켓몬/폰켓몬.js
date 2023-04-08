function solution(nums) {
    // 집합 set 생성
    const pokemons = new Set();
    // nums for문 돌면서 set에 setting
    for (const num of nums) {
        pokemons.add(num);
        if (pokemons.size >= nums.length/2) break;
    }
    // set 길이 반환
    return pokemons.size;
}