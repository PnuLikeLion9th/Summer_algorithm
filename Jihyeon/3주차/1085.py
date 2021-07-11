x, y, w, h = map(int, input().split())
x_min = min(x, w-x)
y_min = min(y, h-y)
if x_min < y_min:
    print(x_min)
else:
    print(y_min)