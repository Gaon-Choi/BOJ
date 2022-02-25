num = int(input())

# first line
print(" " * (num-1), "*", sep='')

a = num - 2; b = 1
for _ in range(num-1):
    print(" " * a, "*", " " * b, "*", sep='')
    a -= 1; b += 2