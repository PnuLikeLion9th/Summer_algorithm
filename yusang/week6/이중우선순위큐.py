import heapq

def solution(operations):
    answer = []
    
    heapq.heapify(answer)
    
    for o in operations :
        if o.find("I") != -1 :
            heapq.heappush(answer, int(o[2:]))
        elif o.find("D 1") != -1 and len(answer) > 0: #최댓값 제거
            answer = heapq.nlargest(len(answer), answer)[1:]
            heapq.heapify(answer)
            
            
        elif o.find("D -1") != -1 and len(answer) > 0: #최솟값 제거
            answer.sort()
            answer = answer[1:]
            
            
    if len(answer) == 0: return [0,0]
    
    return[ sorted(answer)[-1], sorted(answer)[0]]



    #문제점
    #string 배열의 경우 제대로 sort가 되지않음.
    #따라서 int화 시킨 후 queue에 삽입해야함


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))