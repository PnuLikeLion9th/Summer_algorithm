def solution(n,lost,reserve):
    N=[i for i in range(n+2)] #N=[0,1,2,...,n,n+1]
    RB=set((set(reserve)-set(lost)))    #진짜 여분있는 애들 {}
    RL=set((set(lost)-set(reserve))) #체육복 0개인 애들
    hoxy=[] #잃어버린 애들 양 옆
    for i in lost: hoxy.append(i-1), hoxy.append(i+1)
    if n-len(RL)+len(set(hoxy)&RB) >= n: return n   #n보다 크면 여유롭게 빌려줄 수 있다는 의미
    else: return n-len(RL)+len(set(hoxy)&RB)
#최댓값을 구하기 위해 집합의 교집합 연산을 이용했다