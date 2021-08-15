import sys
import heapq

n = int(sys.stdin.readline())
left_heap = []   # 중앙값보다 작은 값 (최대힙)
right_heap = []  # 중앙값보다 큰 값 (최소힙)

for i in range(n):
    x = int(sys.stdin.readline())
    
    if len(left_heap) == len(right_heap) :
        heapq.heappush(left_heap, (-x,x))    # 왼쪽, 오른쪽 길이 같다면 left에 값 저장
    
    else:
        heapq.heappush(right_heap, (x,x)) 

    if len(left_heap) >= 1 and len(right_heap) >= 1 and left_heap[0][1] > right_heap[0][1] :  # 각각의 힙에 원소가 존재하고, left의 최대값 > right의 최소값인 경우
        max = heapq.heappop(left_heap)[1]   # left의 최대값과 right의 최소값 교환
        min = heapq.heappop(right_heap)[1]
        heapq.heappush(left_heap, (-min,min))  
        heapq.heappush(right_heap, (max,max))
    
    print(left_heap[0][1])  # left의 최대값(= 중앙값) 출력