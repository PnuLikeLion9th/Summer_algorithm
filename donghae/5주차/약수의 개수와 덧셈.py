def divisor(n): #약수의 개수 구하는 함수
    l = []  
    for i in range(1, n+1):
        if n % i == 0:     
            l.append(i)   
    return len(l)

def solution(left, right):
    res = 0
    for i in range(left, right+1):
        if divisor(i)%2 == 0:   #짝수인 경우
            res += i
        else:
            res -= i
    return res