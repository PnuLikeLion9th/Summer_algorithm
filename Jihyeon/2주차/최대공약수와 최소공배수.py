def gcd(a,b):                     # 최대공약수 구하기
    if a < b:
        (a, b) = (b, a)           # 앞에 더 큰 값이 오도록 기준을 잡아줌.
    while b != 0:                 # a를 b로 나눈 나머지가 0이 될 때까지 반복
        (a, b) = (b, a%b)         
    return a                      

def lcm(a, b):
    return a*b//(gcd(a,b))        # 최소공배수 구하기