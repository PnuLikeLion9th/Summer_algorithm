temp = 0
n = []
for i in range(10):
    a, b = map(int, input().split())    # a는 타는 사람, b는 내리는 사람 / int형으로 변환
    temp += (b-a)                       # 내리고 탄 후의 사람 수 파악
    n.append(temp)                      # 리스트에 더한 후 최댓값 구하기
print(max(n))