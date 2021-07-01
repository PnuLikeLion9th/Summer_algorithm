def solution(num):
    answer = 0
    
    while answer < 500:
        if num == 1:         # 입력된 수가 1인 경우
            return answer
        
        if num%2 ==0:        # 입력된 수가 짝수인 경우
            num = num/2  
        else:                # 입력된 수가 홀수인 경우
            num = num*3+1  
        answer += 1   
        
    return -1   # 500번 이상 작업하는 경우 -1 리턴