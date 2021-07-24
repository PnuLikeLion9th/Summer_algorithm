#백준 파이썬 50제
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.'''

'''전략: time.strftime('출력한 형식 포맷 코드',time.localtime(time.time()))사용'''

import time  
A = time.strftime('%Y',time.localtime(time.time())) 
B = time.strftime('%m',time.localtime(time.time()))
C = time.strftime('%d',time.localtime(time.time()))

print("%s-%s-%s" %(A,B,C))