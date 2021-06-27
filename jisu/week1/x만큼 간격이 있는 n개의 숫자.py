def solution(x, n):
    answer = [x*i for i in range(1, n+1)]  # i가 1부터 n+1까지 증가함에 따라 x*i 수행
    return answer
