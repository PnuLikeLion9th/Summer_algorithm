def solution(n, m):
    a=n
    b=m
    if n>m:
        n,m = m,n
    while m%n:
        r=m%n
        m=n
        n=r
    return [n, a*b/n]