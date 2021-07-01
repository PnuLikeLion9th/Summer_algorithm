def solution(x):
    sum = 0
    for i in str(x):       # x의 자릿수의 합 계산
        sum = sum + int(i)
        
    if x%sum== 0 :         # x가 자릿수의 합으로 나누어 떨어질 경우
        answer = True
    else :                 # x가 자릿수의 합으로 나누어 떨어지지 않는 경우
        answer = False
        
    return answer