import sys
input = sys.stdin.readline

result = []

while True:
    text = input()
    
    if text == "":
        break
    
    n, s = map(int, text.split())
    
    result.append(s // (n + 1))
    
for elem in result:
    print(elem)