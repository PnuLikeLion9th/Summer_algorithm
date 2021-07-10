def solution(x,n):
    answer=[]
    i=1
    while i <= n:
        k= x*i
        i+=1
        answer.append(int(k))
    return answer