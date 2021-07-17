def solution(n):
    a=0
    k=1
    while True:
        a=a+((n//k)%10)
        if n/k<1:
            break
        k=k*10
    return a