def solution(n, m):
    if n<m:
        for i in range(n,0,-1):
            if n%i==0 and m%i==0:
                high=i
                break
        for a in range(n,(n*m)+1):
            if a%n==0 and a%m==0:
                less=a
                break
        return([high,less])
    elif n>m:
        for i in range(m,0,-1):
            if n%i==0 and m%i==0:
                high=i
                break
        for a in range(m,(n*m)+1):
            if a%n==0 and a%m==0:
                less=a
                break
        return([high,less])