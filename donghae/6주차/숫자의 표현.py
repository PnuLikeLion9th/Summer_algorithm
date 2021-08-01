def solution(n):
    cnt = 0 
    for i in range(1,n+1):
        sum = 0
        while sum <= n: #숫자합이 n보다 작거나 같을 때 까지 반복
            sum += i
            i += 1  #연속한 수만 계산
            if sum == n:    #만약 합과 n이 같으면 카운팅
                cnt += 1
    return cnt