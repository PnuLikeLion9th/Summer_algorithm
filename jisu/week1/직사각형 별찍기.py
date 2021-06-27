a, b = map(int, input().strip().split(' '))
for i in range(b):  # 세로 길이만큼 반복하면서
    print('*'*a)  # a의 길이(가로 길이)만큼 별 출력
