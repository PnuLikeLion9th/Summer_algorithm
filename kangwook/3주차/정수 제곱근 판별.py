import math
def solution(n):
    x=int(math.sqrt(n)) #n에 루트를 씌우면 정수와 소수 두 종류가 나올텐데 이를 다 정수화했다.
    if pow(x,2) == n: #만약 원래 정수였다면 이를 다시 제곱해도 n이 나올 것
        answer=pow(x+1,2)
    else:
        answer=-1
    return answer