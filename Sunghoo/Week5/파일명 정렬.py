import re


def solution(files):

    temp = [re.split("([0-9]+)", file) for file in files]

    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    return [(''.join(s)) for s in sort]


# 정규 표현식과 람다식 , damn pythonic

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
