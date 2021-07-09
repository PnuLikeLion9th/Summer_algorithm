from collections import deque
# queue를 위함


def solution(maps):

    movingUnit = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    height = len(maps)
    width = len(maps[0])

    routeMaps = [[-1 for i in range(width)] for j in range(height)]

    queue = deque()  # 큐 생성
    queue.append([0, 0])  # 시작점 생성
    routeMaps[0][0] = 1  # 시작점 생성

    while queue:
        y, x = queue.popleft()  # 현재 위치

        for direction in movingUnit:
            dy = y + direction[0]
            dx = x + direction[1]
            # 맵 밖으로 나가는지 검사
            if -1 < dy < height and -1 < dx < width:
                # 이동가능한지, 이미 밟은 곳인지 검사
                if maps[dy][dx] == 1 and routeMaps[dy][dx] == - 1:
                    routeMaps[dy][dx] = routeMaps[y][x] + 1
                    # 분신 생성!!!
                    queue.append([dy, dx])
            # 가장 빨리 도달시 바로 return
            if dy == height - 1 and dx == width - 1:
                return routeMaps[height-1][width-1]

    return routeMaps[height-1][width-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
# DFS를 이용한다.
# 1. -1로 된 지도 배열 생성
# 2. 이동할 수 있는 경우의 수가 발생하면 이동 후 좌표를 queue에 삽입
# 3. queue를 모두 꺼내가며 모든 이동을 검토함
# 4. 이동 했을 경우 지도 배열의 각 칸에 카운트를 삽입함. 이동 시 이미 밟혔던 칸이라면 가지 않음
