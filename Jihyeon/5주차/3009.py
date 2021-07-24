x_ = []
y_ = []

for i in range(3):
        x, y = map(int, input().split())
        x_.append(x)
        y_.append(y)

for i in range(3):
        if x_.count(x_[i]) == 1:            # 두 개의 리스트에서 각 인덱스에 위치한 요소의 개수가 한개인지 찾기
                x = x_[i]
        if y_.count(y_[i]) == 1:
                y = y_[i]
print(x, y)