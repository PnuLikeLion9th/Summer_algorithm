def solution(n):
    l = []  
    for i in range(1, n+1):
        if n % i == 0:     #만약 나머지가 0이면(=약수)
            l.append(i)    #리스트에 i 추가
    return sum(l)   #sum함수로 약수의 합 출력