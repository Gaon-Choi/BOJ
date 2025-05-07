def solution(n, costs):
    answer = 0
    
    uf = list(range(n + 1))
    
    def find(x):
        if x == uf[x]:
            return x
    
        root_node = find(uf[x])
        uf[x] = root_node
        
        return root_node

    def union(x, y):
        x_root, y_root = find(x), find(y)
        uf[y_root] = x_root
        
    costs.sort(key = lambda x : x[2])
    
    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost
    
    return answer