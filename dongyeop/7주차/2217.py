n = int(input())
rope = list()
answer = list()
for i in range(n):
   rope.append(int(input()))
rope.sort()
while rope:
    print(n)
    answer.append(rope[0]*n)
    n-=1
    rope.pop(0)


# 모든 로프를 사용할 필요는 없다!

print(max(answer))