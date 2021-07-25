from itertools import combinations


def solution(info, query):

    info_list = []
    for idx, i in enumerate(info):
        info_list.append(i.split(' '))

    query_list = []
    for idx, i in enumerate(query):
        query_ele = i.split(' ')
        while 'and' in query_ele:
            query_ele.remove('and')
        while '-' in query_ele:
            query_ele.remove('-')
        query_list.append(query_ele)
    print(query_list)



    # for query in query_list:
    #     count = 0
    #     for info in info_list:
    #         for n in range(5):
    #             if ((query[n] != '-') and (query[n] != info[n]) and n < 4):
    #                 break
    #             if ((int(query[4]) > int(info[4]))):
    #                 break
    #         else:
    #             count += 1
    #     result.append(count)
    # return result


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))