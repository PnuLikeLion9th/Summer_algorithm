#백준 파이썬 50제-소인수분해
'''정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성, 
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.'''
#3주차 참고

n = int(input())
for i in range(2, n):
	if i*i > n:
		break
	while n%i == 0:
		print(i)
		n //= i
if n > 1: #n이 1보다 크면
    print(n) #n print-for문으로 감쌈