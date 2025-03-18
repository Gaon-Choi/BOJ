n = int(input())
arr = list(map(int, input().split()))

sorted_set = sorted(list(set(arr)))
compressed_elem_list = dict()
comppr = 0

for elem in sorted_set:
    compressed_elem_list[elem] = comppr
    comppr += 1
    
for elem in arr:
    print(compressed_elem_list[elem], end=" ")