def checker(s):
    s = list(s) #문자열 리스트로 변경
    global cnt
    for i in range(len(s)-1): 
        if s[i] != s[i+1]:  #현재 요소와 다음 요소가 다른 경우
            temp = s[i+1:]  #현재 요소 제외하고 슬라이싱 후 temp 변수로 정의
            if temp.count(s[i]) > 0:    #temp 변수에 현재 요소가 하나라도 있으면 0 반환
                return 0
    return 1    #아니면 1 반환 

n = int(input())
cnt = 0
for _ in range(n):
    s = input()
    cnt += checker(s)
print(cnt)