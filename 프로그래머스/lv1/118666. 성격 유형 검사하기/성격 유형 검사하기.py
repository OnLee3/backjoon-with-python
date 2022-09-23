def solution(survey, choices):
    scores = { "R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0 }
    n = len(survey)
    answer = ""
    
    for i in range(n):
        choice = choices[i]
        _survey = survey[i]
        if choice > 4:
            scores[_survey[1]] += (choice-4)
        elif choice < 4:
            scores[_survey[0]] += (4-choice)
            
    if scores["R"] >= scores["T"]:
        answer += "R"
    else:
        answer += "T"
    if scores["C"] >= scores["F"]:
        answer += "C"
    else:
        answer += "F"
    if scores["J"] >= scores["M"]:
        answer += "J"
    else:
        answer += "M"
    if scores["A"] >= scores["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer