from math import gcd                        
def solution(n, m):
#모듈사용
    answer = [gcd(n,m), n*int(m / gcd(n,m))]
    
    
    return answer