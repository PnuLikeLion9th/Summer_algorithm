import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    num = int(input())
    a.append(num)

# 산술평균 구하기
average = round(sum(a)/n)

# 중앙값 구하기
a = sorted(a)
m = a[n//2]

print(average)
print(m)

# 최빈값 구하기
a2 = Counter(a).most_common()

if len(a) > 1:
    if a2[0][1] == a2[1][1]:  # 최빈값이 하나 이상인 경우
        print(a2[1][0])
    else:
        print(a2[0][0])

else:                   # 값이 하나인 경우는 바로 출력
    print(a[0])  

# 범위 구하기
range = max(a) - min(a)
print(range)