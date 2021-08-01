def solution(n, costs):
    state = [0 for n in range(n)]
    costEachIsland = [0 for n in range(n)]
    answer = 0
    
    for e in costs :
        if state[e[0]] == 0 and state[e[1]] == 0 :
            costEachIsland[e[0]] = e[2]
            costEachIsland[e[1]] = e[2]
            state[e[0]] = 1 
            state[e[1]] = 1
            answer = answer + e[2]
        elif state[e[0]] == 0 :
            costEachIsland[e[0]] = e[2]
            costEachIsland[e[1]] = e[2]
            state[e[0]] = 1
            answer = answer + e[2]
        elif state[e[1]] == 0 :
            costEachIsland[e[0]] = e[2]
            costEachIsland[e[1]] = e[2]
            state[e[1]] = 1
            answer = answer + e[2]
        # elif state[e[0]] == 1 and state[e[1]] == 1:
        #     if costEachIsland[e[0]] > e[2] and costEachIsland[e[1]] > e[2]:
        #         costEachIsland[e[0]] = e[2]
        #         costEachIsland[e[1]] = e[2]
        #         state[e[0]] = 1 
        #         state[e[1]] = 1    
    
    
    
    
    
    return answer






print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
