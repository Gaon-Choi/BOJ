T = int(input())

result = []

for _ in range(T):
    n = int(input())
    temp = []
    while (n > 0):
        temp.append(n % 2)
        n //= 2

    result.append(" ".join(str(idx) for idx, value in enumerate(temp) if value == 1))
    
for elem in result:
    print(elem)