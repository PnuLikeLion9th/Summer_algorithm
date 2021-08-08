from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append([0, numbers[0]])   #첫번째 값*(+1,-1) 큐에 넣기
    queue.append([0, -1*numbers[0]]) 
    cnt = 0 #카운트 변수 생성
    while queue:
        step, temp = queue.popleft()    #계산 단계, 합계
        step += 1   
        if step < len(numbers): 
            queue.append([step, temp + numbers[step]])
            queue.append([step, temp - numbers[step]])
        else:   #배열의 길이와 단계 길이가 같은 경우 = 총합
            if temp == target:
                cnt += 1
    return cnt