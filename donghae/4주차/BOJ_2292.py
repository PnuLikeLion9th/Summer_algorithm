n = int(input())
x = 1   #지나는 방 기준(1-7-19-37-61 순)
num = 1 #지나는 방 개수
while n > x:
    x += 6 * num #지나는 방 사이 간격 = 6*num
    num += 1
print(num)