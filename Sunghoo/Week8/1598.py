x, y = map(int, input().split())
전체리스트 = []
# for j in range(y//4 + 1):
#     전체리스트.append([i for i in range(1+4*j,5+4*j)])
if x%4 !=0:
    height_x = x//4
    width_x = x%4 -1
else:
    height_x = (x//4) - 1
    width_x = 3

if y%4 !=0:
    height_y = y//4
    width_y = y%4 -1
else:
    height_y = (y//4) - 1
    width_y = 3
print(abs(width_x - width_y)+abs(height_y - height_x))
# 메모리 초과 (이차원 배열이 너무 길어지는 경우) ==> 애초에 2차원 배열 필요도 없음
