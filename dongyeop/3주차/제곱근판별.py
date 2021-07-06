def solution(n):
    a = pow(n,0.5)#n의 제곱근
    if a == int(a):#정수형과 일치하는지 확인 => 1로 나누어떨어지는 값인지 체크
        return pow(a+1,2)
    else:
        return -1