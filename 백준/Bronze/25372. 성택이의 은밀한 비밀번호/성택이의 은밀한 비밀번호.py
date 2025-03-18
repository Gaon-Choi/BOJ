n = int(input())

result = []

for _ in range(n):
    password = input()
    
    if 6 <= len(password) and len(password) <= 9:
        result.append(True)
    else:
        result.append(False)
        
for elem in result:
    print("yes" if elem else "no")