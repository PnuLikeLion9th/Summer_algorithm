t = int(input())

for i in range(t):
    n = int(input())
                                    # 0일 경우엔 1,0 /1일 경우엔 0,1이 고정
    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")

    else:                           # 3부터는 이전의 값을 이용해 구함
        d = [[0] * 2 for _ in range(n + 1)]
        d[0][0] = 1
        d[1][1] = 1
        d[2] = [1, 1]
        for j in range(3, n + 1):
            d[j][0] = d[j - 1][0] + d[j - 2][0]
            d[j][1] = d[j - 1][1] + d[j - 2][1]

        print("%d %d" % (d[n][0], d[n][1]))