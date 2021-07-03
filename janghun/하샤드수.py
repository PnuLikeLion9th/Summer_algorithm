def solution(x):
    num_1000=x//10**3
    k=x%10**3
    num_100=k//10**2
    k=k%10**2
    num_10=k//10
    num_1=k%10
    sum=num_1000+num_100+num_10+num_1
    if x%sum==0:
        return True
    else:
        return False