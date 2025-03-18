na, nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

hash = dict(zip(A, [1] * len(A)))

for elem in B:
    if elem in hash:
        hash[elem] = 0
        
complement = [key for key, value in hash.items() if value == 1]
complement.sort()

size = len(complement)

print(size)
if size > 0:
    for elem in complement:
        print(elem, end=" ")
    