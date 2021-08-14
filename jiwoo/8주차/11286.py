import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0 :     # x가 0이 아닌 자연수인 경우
        heapq.heappush(heap, (abs(x),x))  # x의 절댓값과 x 추가
    
    else:
        if len(heap) < 1:  # 원소가 없을 경우 0 출력
            print(0)
            
        else:
            print(heapq.heappop(heap)[1])