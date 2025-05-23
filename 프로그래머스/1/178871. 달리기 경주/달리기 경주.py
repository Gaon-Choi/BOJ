def solution(players, callings):
    answer = []
    
    player_dict = dict()
    for idx, player in enumerate(players):
        player_dict[player] = idx
        
    for calling in callings:
        idx = player_dict[calling]
        front_player = players[idx - 1]
        player_dict[calling] -= 1
        player_dict[front_player] += 1
        
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        
    answer = players[:]
    
    return answer