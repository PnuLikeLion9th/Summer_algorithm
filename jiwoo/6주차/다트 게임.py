def solution(dartResult):
    dartResult = dartResult.replace('10','x') 
    result = []
    _sum = []   # 점수 합 
    
    for i in dartResult:     # dartResult의 값들 result에 담아주기
        if i== 'x':          # 'x'인 경우에는 10 추가
            result.append('10')
        else:
            result.append(i)
    
    for i in range(len(result)):
        if result[i] == 'S':
            _sum.append(int(result[i-1]))     # S인 경우에는 그대로 점수 추가
        elif result[i] == 'D':
            _sum.append(int(result[i-1])**2)  # D인 경우에는 제곱해서 점수 추가
        elif result[i] == 'T':
            _sum.append(int(result[i-1])**3)  # T인 경우에는 세제곱해서 점수 추가
        
        if result[i] == '*':
            if len(_sum) < 2:            # 첫번째 기회에서 스타상이 나왔을 경우   
                _sum[-1] = _sum[-1] *2   
            else:
                _sum[-1] = _sum[-1] *2
                _sum[-2] = _sum[-2] *2
                
        elif result[i] == '#':
            _sum[-1] = _sum[-1] * (-1)
    
    return sum(_sum)