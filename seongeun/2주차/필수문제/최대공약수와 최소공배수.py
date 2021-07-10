#최대공약수와 최소공배수
#유클리드 호제법 이용! 
#큰 수를 작은 수로 나누었을 때 나머지가 0이 아니면 작은 수를 큰 수의 자리로, 나머지를 작은 수의 자리로 옮긴 후
#나머지가 0이 될 때까지 이 작업을 계속 반복한다
sssss
def solution(n, m):
    a = n
    b = m

    if n>m:
        (n, m) = (m, n)
    while m%n:
        r = m%n
        m = n
        n = r
    return [n, a*b/n]