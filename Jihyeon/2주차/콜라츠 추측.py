def solution(num):
    anwser = 0

    for i in range(500):

        if(num == 1):                # num이 1인 경우
            return anwser
        
        else:                        # 1이 아닌 경우
            if(num % 2 == 0) :
                num = num/2
                answer += 1
            else:
                num = num*3 + 1
                answer += 1
    return -1