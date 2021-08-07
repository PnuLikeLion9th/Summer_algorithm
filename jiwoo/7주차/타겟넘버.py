# bfs 이용한 방법
def solution(numbers, target):
    answer = 0
    a = [0]                    # 계산한 값들을 넣어줄 리스트
    
    for i in numbers:
        tmp = []               # 계산 값 임시로 저장할 리스트
        for j in a:
            tmp.append(j+i)
            tmp.append(j-i)
        a = tmp
    
    for k in a:                # 타겟넘버와 같은 수 찾기
        if target == k:
            answer += 1
            
    return answer