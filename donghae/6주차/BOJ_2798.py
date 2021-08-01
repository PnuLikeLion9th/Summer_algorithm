n, m = map(int, input().split())
card = list(map(int, input().split()))
l = []
for i in range(n):  #3개 값 합 전부 구하기
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = card[i]+card[j]+card[k]
            if sum <= m:  #합이 m보다 작거나 같으면 l에 추가
                l.append(sum)
print(max(l))   #max값 출력