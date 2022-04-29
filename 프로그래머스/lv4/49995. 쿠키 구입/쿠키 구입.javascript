function solution(cookie) {
    const n = cookie.length;
    let answer = 0;
    
    for (let l=0; l<n-1; l++){
        let m = l;
        let r = l+1;
        let big = cookie[m];
        let small = cookie[r];
        while (m < n && r < n){
            if (big === small) answer = Math.max(answer, big);
            if (big <= small){
                m++;
                if (m < n){
                    big += cookie[m];
                    small -= cookie[m];
                }
                if (m === r){
                    r++;
                    if (r < n) small += cookie[r];
                }
            }
            else if (big > small){
                r++;
                if (r < n) small += cookie[r];
            }
        }
    }
    
    return answer;
}