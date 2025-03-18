n = int(input())

gap = n - 1
inner_gap = 1

print(" " * gap, "*", sep="")

gap -= 1

for i in range(n-2):
    print(" " * gap, "*", " " * inner_gap, "*", sep="")
    gap -= 1
    inner_gap += 2

if n != 1:    
    print("*" * (2 * n - 1))