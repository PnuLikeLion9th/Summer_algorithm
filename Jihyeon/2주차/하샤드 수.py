def solution(X):
    sum = 0

    for i in str(x):
        sum += int(i)         # 각 자릿수 더하기
    
    if(x%sum == 0):           # x가 더한 자릿수 값으로 나누어 떨어지면
        return True
    else:
        return False