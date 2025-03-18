import sys
input = sys.stdin.readline

result = []

while True:
    n = input()
    
    if n == "":
        break
    
    n = int(n)
    
    size = 1
    
    while True:
        if int('1' * size) % n == 0:
            break
        size += 1
        
    result.append(size)
    
for elem in result:
    print(elem)