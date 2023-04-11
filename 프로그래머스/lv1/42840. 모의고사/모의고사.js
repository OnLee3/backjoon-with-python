function solution(answers) {
    const answer = [];
    const patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ];
    const scores = [0, 0, 0];

    for (const [i, answer] of answers.entries()) {
        for (const [j, pattern] of patterns.entries()) {
            if (answer === pattern[i % pattern.length]) {
                scores[j]++;
            }
        }
    }
    
    const maxScore = Math.max(...scores);
    for (const [i, score] of scores.entries()) {
        if (maxScore === score) {
            answer.push(i+1);
        }
    }
    
    return answer;
}