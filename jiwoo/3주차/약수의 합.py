def solution(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:      # i로 나누었을 때 나머지 0인 경우(약수인 경우)     
            sum += i        # 약수 합하기
    return sum