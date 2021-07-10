# 프로그래머스_정수 제곱근 판별_수학_레벨 1
# sqrt함수를 이용해서 n의 제곱근을 구한다.
# 이때 n의 제곱근이 실수형태로 나타나는것을 이용하여 n이 양의 정수 x의 제곱인지를 판별한다

import math


def solution(n):
    num = math.sqrt(n)
    if num == int(num):  # n의 제곱근 num이 정수일때, 즉 x의 제곱일때 (num+1)^2 해서 return 한다
        return (num+1)**2
    else:  # n의 제곱근 num이 실수일때 (ex 루트2는 1.414... 형태) -1을 return 한다
        return -1


print(solution(3))
