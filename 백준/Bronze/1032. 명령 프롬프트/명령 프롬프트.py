n = int(input())

words = []
for _ in range(n):
    words.append(input())
    
size = len(words[0])

answer = ""

for i in range(size):
    tmp = words[0][i]
    flag = False
    
    for j in range(n):
        if tmp != words[j][i]:
            flag = True
            break
        
    if flag:
        answer += "?"
    else:
        answer += tmp
        
print(answer)