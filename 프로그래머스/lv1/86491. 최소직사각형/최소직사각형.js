function solution(sizes) {
    let maxWidth = 0;
    let maxHeight = 0;
    
    for (const size of sizes) {
        let [width, height] = size;
        if (width < height) {
            const tmp = width;
            width = height;
            height = tmp;
        }
        maxWidth = Math.max(width, maxWidth);
        maxHeight = Math.max(height, maxHeight);
    }
    
    return maxWidth * maxHeight;
}