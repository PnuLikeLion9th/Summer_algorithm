from math import sqrt
def solution(n):
    answer=0
    def primary(n):#소수 판별기 함수
        for i in range(2,int(sqrt(n))+1):#2부터 n의 제곱근까지의수를
            if n%i ==0:#n에 나누어서 나누어떨어지면 소수가 아님
                return False
        return True#그게 아니면 소수
    for i in range(2,n+1):#1은 어짜피 소수가 아니므로 2부터 검사
        if primary(i):
            answer +=1
    print(answer)
    
#에라토스테네스의 체
def solution(n):
    s = [True]*(n+1)#true가 n+1개 담긴 리스트 만듬
    m = int(n**0.5)
    for i in range(2,m+1):#리스트를 돌면서
        if s[i]==True:#소수가 되는 녀석을 만나면
            for j in range(2*i,n+1,i):#그녀석의 배수들은 모두 false로 바꿔줌
                s[j] = False
    answer=[i for i in range(2,n+1) if s[i]==True]
    return len(answer)