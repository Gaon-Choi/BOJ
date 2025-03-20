def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    size = len(truck_weights)
    curr_cnt = 0
    
    before_dari = [0] * bridge_length
    after_dari = []
    
    total_weight = 0
    
    while len(after_dari) < size:
        # 다리에서 트럭 하나씩 이동
        head = before_dari.pop(0)   # -
        
        answer += 1

        if head != 0:
            after_dari.append(head)
            total_weight -= head
            curr_cnt -= 1
            
        next_truck = 0
        
        # 다리에 트럭 싣기
        if truck_weights and (total_weight + truck_weights[0] <= weight) and (curr_cnt < bridge_length):
            next_truck = truck_weights.pop(0)
            
            total_weight += next_truck
            curr_cnt += 1
            
        before_dari.append(next_truck)   # +
    
    return answer