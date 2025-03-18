N = int(input())
text = input()

a = 0; b = 0

for c in text:
    if c == "A":
        a += 1
    elif c == "B":
        b += 1
        
print("B" if b > a else "A" if a > b else "Tie")