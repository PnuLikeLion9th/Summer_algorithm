import re


def solution(files):
    filtered_files = [re.split("([0-9]+)", file) for file in files]
    sorted_files = sorted(filtered_files, key=lambda x: (x[0].lower(), int(x[1])))
    return [(''.join(s)) for s in sorted_files]


files = ["img12.png", "img10.pn21g", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
solution(files)
