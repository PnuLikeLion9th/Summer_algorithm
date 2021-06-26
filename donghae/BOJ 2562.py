max = 0
for i in range(9):  #입력값 9번 받기
    n = int(input())
    if n > max:
        max = n
        max_num = i
        continue
    i += 1
print(max)  #최댓값 및 순서 출력
print(max_num+1)
