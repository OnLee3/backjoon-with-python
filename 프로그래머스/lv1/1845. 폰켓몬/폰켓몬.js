function solution(nums) {
    const uniquePokemons = new Set(nums);
    return Math.min(uniquePokemons.size, nums.length / 2);
}
