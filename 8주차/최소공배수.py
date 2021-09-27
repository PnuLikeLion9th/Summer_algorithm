#백준 파이썬 기초 50제
'''두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.'''

n = int(input())

def gcd(a, b) :
    if b==0:
        return a
    else :
        return gcd(b,a%b)

for _ in range(n):
    a , b = map(int,input().split())
    g  = gcd(a,b)
    print(int(g*(a/g)*(b/g)))