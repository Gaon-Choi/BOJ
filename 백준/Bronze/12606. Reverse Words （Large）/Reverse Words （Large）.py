import sys
sys = sys.stdin.readline

n = int(input())

result = []

for _ in range(n):
    text = input().split()
    text.reverse()
    result.append(text)
    
for i in range(len(result)):
    print("Case #{idx}: {elems}".format(idx=i+1, elems=" ".join(result[i])))