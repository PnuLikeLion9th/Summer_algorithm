#ceil을 사용하기 위함
#ceil은 소수점 올림 함수
import math

def solution(progresses, speeds):
    answer = []
    beforeProgressCompleteDay = -1 #이전 작업이 끝나는 일자
    for i in range(len(progresses)) : #progress를 모두 탐색
        #작업의 소요 일자
        currentProgressDay = math.ceil((100 - progresses[i] )/ speeds[i])
        
        #이전 작업보다 빨리 끝난다면 이전 작업과 합쳐줌
        if beforeProgressCompleteDay >= currentProgressDay :
            answer[-1] = answer[-1] + 1
        else:
        #이전 작업보다 늦게 끝난다면 push
            beforeProgressCompleteDay = currentProgressDay
            answer.append(1)
    return answer


print(solution[[95, 90, 99, 99, 80, 99], [1,30,5]])