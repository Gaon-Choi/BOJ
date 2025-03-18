n = int(input())

ten_square = len(str(n))

total = 0

for i in range(1, ten_square):
    total += ((10 ** i) - (10 ** (i - 1))) * i
    
total += (n - (10 ** (ten_square - 1)) + 1) * ten_square

print(total)