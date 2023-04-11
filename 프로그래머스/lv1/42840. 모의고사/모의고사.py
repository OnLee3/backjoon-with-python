def solution(answers):
    answer = []
    first_solver = [1, 2, 3, 4, 5]
    second_solver = [2, 1, 2, 3, 2, 4, 2, 5]
    third_solver = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = dict({ '1': 0, '2': 0, '3': 0 })
    
    for i in range(len(answers)):
        first_solver_idx = i % len(first_solver)
        second_solver_idx = i % len(second_solver)
        third_solver_idx = i % len(third_solver)
        
        if answers[i] == first_solver[first_solver_idx]:
            scores['1'] += 1
        if answers[i] == second_solver[second_solver_idx]:
            scores['2'] += 1
        if answers[i] == third_solver[third_solver_idx]:
            scores['3'] += 1
    
    max_score = max(scores.values())
    for idx, score in scores.items():
        if score == max_score:
            answer.append(int(idx))
    return answer