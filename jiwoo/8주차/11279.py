import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())

    if x != 0 :     # x가 0이 아닌 자연수인 경우
        heapq.heappush(heap,(-x,x))   # 힙에 x 추가

    else:
        if len(heap) < 1 :   # 배열 비어있는 경우 0 출력
            print(0)

        else:
            print(heapq.heappop(heap)[1])   # 입력된 값 출력해야하므로 두번째 값 출력