def find_num(x):
    if x in arr:
        return arr[x]
    
    arr[x] = find_num(x // p) + find_num(x // q)

    return arr[x]

n, p, q = map(int, input().split())

arr = dict()
arr[0] = 1

print(find_num(n))