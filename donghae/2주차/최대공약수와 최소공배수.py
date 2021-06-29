def gcd(x, y):  #최대공약수
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):  #최소공배수
    return x * y // gcd(x, y)

def solution(x, y):
    return [gcd(x,y), lcm(x,y)]