def solution(n):
    sum = 0
    for i in range(1,n+1):#1부터 자기자신까지 범위에서
        if n%i==0:#나누어 떨어지는놈은
            sum+=i#n의 약수니까 더해줌
    return sum