import sys
input = sys.stdin.readline

def is_valid(text):
    cnt = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')

    if cnt == 0:
        return False
    
    if len(text) - cnt < 2:
        return False
    
    return True

def combination(arr, k):
    result = []
    comb = []

    def backtrack(start):
        if len(comb) == k:
            if is_valid(comb):
                result.append(comb[:])
            return
        
        for i in range(start, n):
            comb.append(arr[i])
            backtrack(i + 1)
            comb.pop()

    backtrack(0)

    return result

l, n = map(int, input().split())
arr = input().split()
arr.sort()

result = combination(arr, l)

for res in result:
    print("".join(res))