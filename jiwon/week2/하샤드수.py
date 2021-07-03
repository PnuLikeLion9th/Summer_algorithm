def solution(x):
    n=x # 처음 x 값 그대로 사용하면 0될 때 처음 x 값 알수없음
    sum=0
    while n>0:
        sum+=n%10 # % : 나머지 연산
        n=n//10 # // : 나머지 후 몫만
    
    if x%sum==0:
        return True
    else:
        return False