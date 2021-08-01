def solution(n, lost, reserve):    
    new_lost = set(lost) - set(reserve)        # 체육복 잃어버린 학생이 여분의 체육복 있을 경우 제거
    new_reserve = set(reserve) - set(lost)
    
    num = n - len(new_lost)    # num = 체육수업을 들을 수 있는 학생의 수
    
    for i in new_lost:
               
        if (i-1) in new_reserve:     # 여분의 체육복을 구했을 경우
            num += 1                 # 수업 들을 수 있는 학생 수 +1
            new_reserve.remove(i-1)  # 여분의 체육복 빌려줬으므로 제거
        elif (i+1) in new_reserve:
            num += 1
            new_reserve.remove(i+1)
            
    return num