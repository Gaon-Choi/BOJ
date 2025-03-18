n = int(input())

result = []

for _ in range(n):
    text = input()
    
    consonauts = 0
    vowels = 0
    
    for c in text:
        if c.isalpha():
            if c in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
                vowels += 1
            else:
                consonauts += 1

    result.append([consonauts, vowels])
    
for elem in result:
    print(elem[0], elem[1])