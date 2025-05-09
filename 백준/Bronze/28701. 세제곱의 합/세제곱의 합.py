import sys
input = sys.stdin.readline

n = int(input())

one = 0
two = 0
three = 0

for i in range(1, n + 1):
    one += i
    two += i
    three += i ** 3

two = two * two

print(one, two, three, sep="\n")