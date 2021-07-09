
import re
    # for i in re.findall('^[a-z]|\s[a-z]', s):


def reorderLogFiles(logs):  
    littersLogs = list(filter(lambda x: re.match('[A-Z]|[a-z]', x.split()[1]), logs))
    digitLogs = list(filter(lambda x: re.match('[0-9]', x.split()[1]), logs))


    littersLogs = list(map(lambda x : x.split(),littersLogs))
    digitLogs = list(map(lambda x : x.split(),digitLogs))

    littersLogs.sort(key = lambda x : (x[1:], x[0]))

    answer = littersLogs + digitLogs

    return list(map(lambda x : ','.join(x).replace(',' , ' '),answer))

# print(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))



#틀린 이유
#1. digital logs는 입력 순서대로 출력하면된다.
#2. sort의 방식 x[1:-1]이 아니라 x[1:]로 해야한다.