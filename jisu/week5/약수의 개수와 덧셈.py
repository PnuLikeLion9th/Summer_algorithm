def solution(left, right):
    answer = 0
    cnt=0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i%j == 0: 
                cnt+=1 #약수 카운팅
        answer=answer-i if cnt%2 else answer+i #약수 개수가 홀수면 빼기, 짝수면 더하기
        cnt=0 #cnt 초기화
    return answer