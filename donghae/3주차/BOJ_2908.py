a, b = input().split()
def x(n):   #숫자 거꾸로 만드는 함수
    n = list(n) #리스트로 변경 후 reverse 함수 사용
    n.reverse()
    return int(''.join(n))
print(x(a) if x(a) >= x(b) else x(b))