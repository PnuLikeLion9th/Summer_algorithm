#2.콜라츠추측

def solution(num):
    answer = 0 #0으로 시작
    
    while num != 1: 
        if num % 2 == 0: #짝수일 경우 2로 나눔
            num = num/2
        else:
            num = 3*num + 1 #홀수일 경우 3을 곱한 뒤 1을 더함
        answer += 1 #처리 횟수 카운팅

    if answer >= 500: #500 이상 했을때는 -1을 리턴
            return -1
    return answer







    for i in range(500):
        if num % 2 == 0:
            num = num/2
            answer += 1

        if num % 2 == 0:
            num = (num*3)+1
            answer += 1

        if answer > 500:
            answer = -1

    return answer
        
            

    
    
    return answer
