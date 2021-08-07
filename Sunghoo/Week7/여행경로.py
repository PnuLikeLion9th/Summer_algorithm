from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['ICN'],
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]
