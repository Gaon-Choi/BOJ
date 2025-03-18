winner = -1
total = 0

for i in range(5):
    total_ = sum(list(map(int, input().split())))
    if total_ > total:
        total = total_
        winner = i + 1
        
print(winner, total)