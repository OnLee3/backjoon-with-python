function solution(sequence, k) {
    let start = 0;
    let end = 0;
    let currentSum = sequence[0];
    const answerList = [];

    while (start < sequence.length && end < sequence.length) {
        if (currentSum === k) {
            answerList.push([[start, end], end - start]);
            currentSum -= sequence[start];
            start++;
        } else if (currentSum < k) {
            end++;
            if (end < sequence.length) {
                currentSum += sequence[end];
            }
        } else {
            currentSum -= sequence[start];
            start++;
        }
    }
    answerList.sort((a, b) => {
        if (a[1] >= b[1]) return 1;
        return -1;
    });
    return answerList[0][0];
}
