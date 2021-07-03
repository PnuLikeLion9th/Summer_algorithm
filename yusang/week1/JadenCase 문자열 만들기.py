# #방법1

# def solution(s):
#     s = list(s.lower())
#     s[0] = s[0].upper()
#     start = 0
#     while True:
#         try:
#             index = s.index(' ', start)
#             s[index + 1] = s[index + 1].upper()
#             start = index + 1
#         except:
#             break
#     return ''.join(s)


# #방법2

import re

def solution(s):
    s= s.lower()
    #'^[a-z] 첫문자 + 알파벳
    #\s[a-z] 공백문자 + 알파벳
    for i in re.findall('^[a-z]|\s[a-z]', s):
       s =  s.replace(i, i.upper(), 1)
    return  s

print(solution("AAAAA AAAA"))
