def solution(num):
    if num==1:
        return 0
    for i in range(500): #500번 시도했을 때 최종 1이 되려면
        if num % 2==0: #짝수이면
            num = num / 2 #또 2로 나누고
        else: #짝수가 아니면
            num = num*3 + 1 

        if num ==1: 
            return i + 1

    return -1