#모의고사

def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    a1,a2,a3 = 0,0,0
    
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10

        if p1[s1] == answers[i]:
            a1 += 1
        if p2[s2] == answers[i]:
            a2 += 1
        if p3[s3] == answers[i]:
            a3 += 1
    
    k=max(a1,a2,a3)
    answer=[]

    if k == a1:
        answer.append(1)
    if k == a2:
        answer.append(2)
    if k == a3:
        answer.append(3)
    
    return answer
          
#if 넣는거랑 elif 넣는거랑 차이점 뭔지 모르겠음
