a, b = map(int, input().strip().split(' '))
for i in range(b):	#세로 길이만큼 반복
    for j in range(a):	#가로 길이만큼 별찍기
        print('*', end='')
    print()	#줄바꿈`