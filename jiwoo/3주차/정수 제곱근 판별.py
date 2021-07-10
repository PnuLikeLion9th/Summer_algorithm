def solution(n): 
    for i in range(1,n+1):
        if i**2 == n:          # i를 제곱한 수가 n이라면,
            return (i+1)**2    # i에 1을 더한 후, 제곱해 리턴
    return -1    # 정수의 제곱 아니라면, -1 리턴