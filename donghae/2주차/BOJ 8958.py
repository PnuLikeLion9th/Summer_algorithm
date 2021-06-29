# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

n = int(input())    #테스트 케이스 개수 받기
score = 0
sum = 0
for i in range(n):   
    s = input()    #OX문자열 입력받기
    for j in range(len(s)):
        if s[j] == 'O':    
            score += 1  #'O'인 경우 1 더하기
            sum += score       
        else:
            score = 0   #'X'인 경우 score 0으로 초기화
    print(sum)
    sum = 0
    score = 0