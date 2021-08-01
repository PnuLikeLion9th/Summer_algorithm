def solution(answers):
    score = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    c1 = c2 = c3 =0
    for i in range(len(answers)):
        if answers[i] == p1[i%len(p1)]:
            c1+=1
        if answers[i] == p2[i%len(p2)]:
            c2+=1
        if answers[i] == p3[i%len(p3)]:
            c3+=1
    score+=[c1,c2,c3]
    answer = []
    maxscore = max(score)
    for person,correct in enumerate(score):
        if correct == maxscore:
            answer.append(person+1)
    return answer