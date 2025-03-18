a, b = input().split()

A = list(map(int, list(a)))
B = list(map(int, list(b)))

# 자릿수가 0인 경우는 모두 제외함
A = list(filter(lambda x : x != 0, A))
B = list(filter(lambda x : x != 0, B))

total = sum(A) * sum(B)

'''
for x in A:
    for y in B:
        total += x * y
'''

print(total)