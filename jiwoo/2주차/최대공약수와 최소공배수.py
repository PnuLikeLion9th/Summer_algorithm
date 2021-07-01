def solution(n, m):
    for i in range(min(n,m),0,-1):    # n,m 중 작은 수부터 1씩 줄여나가며 최대공약수 찾기
        if n%i == 0 and m%i == 0:
            GCD = i
            break
    LCM = (n*m)/GCD        # 최대공약수 이용해서 최소공배수 구하기
    
    answer = [GCD,LCM]
    return answer