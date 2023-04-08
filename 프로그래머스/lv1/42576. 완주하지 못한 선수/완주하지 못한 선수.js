function solution(participant, completion) {
    const participants = {};
    const completions = {};
    
    for (let i = 0; i < participant.length; i++) {
        if (participants.hasOwnProperty(participant[i])) {
            participants[participant[i]]++;
        } else {
            participants[participant[i]] = 1;
        }
        if (i !== participant.length - 1) {
            if (completions.hasOwnProperty(completion[i])) {
                completions[completion[i]]++;
            } else {
                completions[completion[i]] = 1;
            }
        }
    }
    
    for (let i = 0; i < completion.length; i++) {
        participants[completion[i]] -= 1;
    }
    for (let i = 0; i < participant.length; i++) {
        if (participants[participant[i]]) {
            return participant[i];
        }
    }
}