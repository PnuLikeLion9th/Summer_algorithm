from collections import deque


def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    new_id2 = ''
    for i in new_id:
        if i.isalnum() or i in ["-", "_", "."]:
            new_id2 += i

    # 3,
    new_id2 = deque(new_id2)
    new_id3 = deque(new_id2.popleft())
    while len(new_id2) > 0:
        i = new_id2.popleft()
        if i == "." and new_id3[-1] == i:
            pass
        else:
            new_id3.append(i)
    if new_id3[0] == ".":
        new_id3.popleft()
    if new_id3[-1] == ".":
        new_id3.pop()

    if not new_id3:
        new_id3 = 'a'

    new_id3 = list(new_id3)
    if len(new_id3) > 15:
        new_id3 = deque(new_id3[:15])
        if new_id3[-1] == ".":
            new_id3.pop()
    if len(new_id3) <= 2:
        while len(new_id3) != 3:
            new_id3.append(new_id3[-1])
    return ''.join(list(new_id3))
