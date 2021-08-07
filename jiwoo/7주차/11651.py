import sys

n = int(sys.stdin.readline())
nums = []

for i in range(n):
    [x,y] = map(int,sys.stdin.readline().split())   # 좌표 받아와서 리스트 형태로 저장
    nums.append([x,y])

nums = sorted(nums, key= lambda x: (x[1],x[0]))   # y좌표 증가순으로 정렬

for i in range(n):
    print(nums[i][0], nums[i][1])   # x좌표, y좌표 순으로 출력