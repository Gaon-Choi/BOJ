n = int(input())

result = 1

for i in range(2, n + 1):
    result *= i
    while True:
        if result % 10 != 0:
            break
        result = result // 10
        
    result = result % 100000000000000
        
print(str(result)[-5:])