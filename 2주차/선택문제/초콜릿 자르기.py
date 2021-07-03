#백준 50제 2063번 초콜릿 자르기

n, m = input().split()

n = int(n)
m = int(m)

if n >= m:
    print((m-1)+(n-1)*m)
else:
    n, m = m,n
    print((m-1)+(n-1)*m)
