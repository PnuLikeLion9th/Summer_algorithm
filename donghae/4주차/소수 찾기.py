def solution(n):
    num = set(range(2, n+1))
    #2부터 n까지의 집합 num 만들기
    
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i)) 
            #에라토스테네스의 체, i의 배수를 num에서 제거
            #range(start, stop, step)
    return len(num)