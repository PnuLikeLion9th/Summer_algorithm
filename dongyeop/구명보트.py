from collections import deque
def solution(people,limit):
    people.sort()
    people=deque(people)
    count = 0
    #가장 가벼운 사람과 가장 무거운 사람을 보트에 같이 태울경우가 최소값을 뽑아낸다.
    #가장 가벼운 사람과 가장무거운 사람의 무게가 limit을 넘지않으면 같이 보트에 태우고
    #그게 아니면 무거운 사람 혼자 태운다.

    while people:#리스트가 빌때까지 반복
        if len(people)>=2:#혼자 남게 될 경우를 고려해서 리스트의 길이가 2이상일때 조건을 걸었다.
            if people[-1]+people[0]<=limit:
                people.popleft()
                people.pop()
                count+=1
            else: 
                people.pop()
                count+=1
        else:
            people.pop()
            count+=1
    return count
#deque안쓰고 푸니까 시간초과에 걸렸다.pop(0)는 시간복잡도가 o(n)인데 반해 popleft()는 시간복잡도가 o(1)이다.
solution([70,80,50,50],100)