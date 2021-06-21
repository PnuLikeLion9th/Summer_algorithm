# 프로그래머스_직사각형 별찍기_문자열_레벨 1
# 기본적인 반복문 사용 문제

a, b = map(int, input().strip().split(' '))

for _ in range(b):  # b만큼 반복하는 for문
    print("*"*a)  # a만큼 별을 찍어낸다
