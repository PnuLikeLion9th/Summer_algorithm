def solution(n,m):
    def gcl(a,b):#유클리드 호재법을 이용하여 최대공약수를 뽑아내는 함수이다.
        while a%b !=0:#유클리드 호재법은 두수를 나누어 나머지가 0이 되지 않는다면 나누는수를 나누어지는 수에 넣고 나머지를 나누는 수 자리에 넣는 행동을 반복한다.
            a,b = b,a%b
        return b
    def lcm(a,b):#두수의 곱을 최대공약수로 나눈 몫은 최소공배수이다.
        return a*b//gcl(a,b)
    return [gcl(n,m),lcm(n,m)]