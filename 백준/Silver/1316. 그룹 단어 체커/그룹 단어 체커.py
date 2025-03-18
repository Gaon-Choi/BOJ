def is_group_word(word: str):
    alphabet = []
    alphabet.append(word[0])

    for c in word:
        if alphabet[-1] == c:
            continue
        else:
            alphabet.append(c)
    
    if len(alphabet) == len(set(alphabet)):
        return True
        
    return False
    
n = int(input())

answer = 0

for _ in range(n):
    word_ = input()
    
    if is_group_word(word_):
        answer += 1
        
print(answer)