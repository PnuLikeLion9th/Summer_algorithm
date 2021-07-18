def in_range(x, y):
    SIZE = 5
    return -1 < x < SIZE and -1 < y < SIZE


def check(r, c, p):
    dist = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in dist:
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and p[nx][ny] == 'P':
            return False

    dist = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in dist:
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and p[nx][ny] == "P" and (p[r][ny] != "X" or p[nx][c] != "X"):
            return False

    dist = [(2, 0), (0, 2), (-2, 0), (0, -2)]
    for dx, dy in dist:
        nx, ny = r + dx, c + dy
        if in_range(nx, ny) and p[nx][ny] == "P" and p[r + dx // 2][c + dy // 2] != "X":
            return False

    return True


def solution(places):
    answer = []
    entire_matrix = [(i, j) for i in range(5) for j in range(5)]
    for place in places:
        for r, c in entire_matrix:
            if place[r][c] == 'P' and not check(r, c, place):
                answer.append(0)
                break
        else:
            answer.append(1)

    return answer