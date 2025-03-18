score_a = 100
score_b = 100

num = int(input())
for i in range(num):
    a, b = (input()).split()
    a = int(a); b = int(b)
    if a < b:
        score_a -= b
    elif a > b:
        score_b -= a
    else:
        continue
print(score_a, score_b, sep="\n")