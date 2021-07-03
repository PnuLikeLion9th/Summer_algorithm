직사각형별찍기.py

a, b = map(int, input().strip().split(' '))
for x in range(b):	#세로 
    for y in range(a):	#가로 
        print('*', end='')
    print()	
