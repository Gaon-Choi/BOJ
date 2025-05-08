def solution(score):
    answer = []
    
    for idx, s in enumerate(score):
        s.append(idx)
        s.append(0)
        
    score.sort(key = lambda x : -(x[0] + x[1]))
    rank = 0
    prev = [0, 0]
    
    for i in range(len(score)):
        if sum(prev) != sum(score[i][0:2]):
            score[i][3] = i + 1
            rank = i + 1
            prev = score[i][0:2][:]
        else:
            score[i][3] = rank
    
    score.sort(key = lambda x : x[2])
    
    for s in score:
        answer.append(s[3])
    
    return answer