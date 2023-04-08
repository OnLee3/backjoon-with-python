def solution(players, callings):
    playerIndicies = {}
    
    for i in range(len(players)):
        playerIndicies[players[i]] = i
    
    for i in range(len(callings)):
        calledPlayer = callings[i]
        calledPlayerIdx = playerIndicies[calledPlayer]
        
        if (calledPlayerIdx > 0):            
            tmp = players[calledPlayerIdx - 1]
            players[calledPlayerIdx - 1] = calledPlayer
            players[calledPlayerIdx] = tmp
            
            playerIndicies[calledPlayer] = calledPlayerIdx - 1
            playerIndicies[tmp] = calledPlayerIdx
        
    return players