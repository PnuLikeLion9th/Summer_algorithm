n = int(input())
d = [0] * (n + 1)	                        # d에 계산된 값을 저장. n + 1 -> 1번째 수는 d[2], 계산하기 편하게 d[1]을 1번째 인 것 처럼 만들어 줌

for i in range(2, n + 1): 
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)	     # d[i]에 1을 더하지 않는 이유는 이미 1을 뺄 때 더해줬기 때문
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])