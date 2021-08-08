n = int(input())    #참여하는 사람 수 

def money():    #금액을 반환하는 함수 만들기
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:  #같은 눈이 4개
        return 50000 + lst[0] * 5000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]: return 10000+ lst[1] * 1000  #같은 눈이 3개
        return 2000 + (lst[1] +  lst[2]) * 500  #같은 눈이 2개씩 두 쌍
    for i in range(3): 
        if lst[i] == lst[i+1]: return 1000 + lst[i] * 100   #같은 눈이 2개
    return lst[-1] * 100    #같은 눈 없음

print(max(money() for i in range(n)))   #사람 수 만큼 함수 실행 후 최댓값 반환

