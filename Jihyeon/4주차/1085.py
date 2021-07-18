# 임의의 좌표(X,Y)에서 경계선까지의 최솟값 구하기
# (X,Y)에서 (0,0)까지 긋고 원 그린다고 가정
# X, Y, W-X, H-Y 중 최솟값 구하기

x, y, w, h = list(map(int, input().split())) 
print(min([x, y, w - x, h - y]))

