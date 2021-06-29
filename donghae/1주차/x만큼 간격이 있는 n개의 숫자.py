def solution(x, n):
    answer = []
    for i in range(1,n+1):  #1부터 n까지
        answer.append(x*i)  #리스트에 x*i값 추가
    return answer