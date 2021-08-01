def solution(answers):
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    sum1,sum2,sum3 = 0,0,0
    result = []
    
    for i in range(len(answers)):
        if answers[i] == num1[i%5]:  # 1번 수포자의 답 비교 과정 
            sum1 += 1
        if answers[i] == num2[i%8]:  # 2번 수포자의 답 비교 과정
            sum2 += 1
        if answers[i] == num3[i%10]: # 3번 수포자의 답 비교 과정
            sum3 += 1
    
    max_sum = max(sum1,sum2,sum3)    # 가장 많은 문제를 맞힌 사람의 점수
    if max_sum == sum1:              # 1번 수포자의 점수가 최고점일 경우 result에 추가 
        result.append(1)
    if max_sum == sum2:              # 2번 수포자의 점수가 최고점일 경우 result에 추가
        result.append(2)
    if max_sum == sum3:              # 3번 수포자의 점수가 최고점일 경우 result에 추가
        result.append(3)
    
    return result