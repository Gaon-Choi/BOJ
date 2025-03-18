T = int(input())

result = []

for _ in range(T):
    y = 0; k = 0;
    
    for _ in range(9):
        a, b = map(int, input().split())
        y += a
        k += b
            
    result.append("Yonsei" if y > k else "Korea" if k > y else "Draw")
    
for elem in result:
    print(elem)