# counting sort 이용해서 풀이
import sys
n = int(sys.stdin.readline())
tmp = [0] * 10001    # 숫자의 빈도를 저장할 리스트

for i in range(n):
    before = int(sys.stdin.readline())
    tmp[before] += 1     # input으로 받은 수의 빈도 추가

for i in range(1,len(tmp)):
    for j in range(tmp[i]):  # 빈도 수 만큼 인덱스 값 출력
        print(i)