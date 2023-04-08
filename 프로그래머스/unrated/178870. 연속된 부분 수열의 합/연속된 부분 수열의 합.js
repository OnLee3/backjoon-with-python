function solution(sequence, k) {
    let start = 0;
    let end = 0;
    let currentSum = sequence[0];
    let minLength = Infinity;
    let bestAnswer;

    while (start < sequence.length && end < sequence.length) {
        if (currentSum === k) {
            const length = end - start;
            if (length < minLength) {
                minLength = length;
                bestAnswer = [start, end];
            }
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

    return bestAnswer;
}
