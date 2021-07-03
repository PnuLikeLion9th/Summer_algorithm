def solution(n):
    a=n//10000
    b=(n-a*10000)//1000
    c=(n-(a*10000+b*1000))//100
    d=(n-(a*10000+b*1000+c*100))//10
    e=(n-(a*10000+b*1000+c*100+d*10))//1
    k=int(a+b+c+d+e)
    if n%k==0:
        answer = True
    else :
        answer = False
    return answer
# if n%k==0:
#     print(str(n)+'의 모든 자릿수의 합은 '+str(k)+'입니다. '+str(n)+'은 '+str(k)+'로 나누어 떨어지므로 '+str(n)+'은 하샤드 수입니다.')
# else:
#     print(str(n)+'의 모든 자릿수의 합은 '+str(k)+'입니다. '+str(n)+'은 '+str(k)+'로 나누어 떨어지지 않으므로 '+str(n)+'은 하샤드 수가 아닙니다.')
   