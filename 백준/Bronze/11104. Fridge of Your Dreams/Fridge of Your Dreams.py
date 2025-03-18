N = int(input())

result = []

for _ in range(N):
    bin_num = reversed(list(input()))
    total = 0
    
    for i, v in enumerate(bin_num):
        total += 2 ** i if v == "1" else 0
        
    result.append(total)
    
for elem in result:
    print(elem)