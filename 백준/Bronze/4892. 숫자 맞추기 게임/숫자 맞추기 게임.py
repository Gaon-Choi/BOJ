result = []

while True:
    n0 = int(input())
    
    if n0 == 0:
        break
    
    n1 = 3 * n0
    
    n2 = (n1 // 2) if (n1 % 2 == 0) else (n1 + 1) // 2
    
    n3 = 3 * n2
    
    n4 = n3 // 9
    
    result.append([n1 % 2 != 0, n4])
    
for idx, elem in enumerate(result):
    print("{idx}. {is_n2_odd} {n4}".format(idx=idx+1, is_n2_odd = "odd" if elem[0] else "even", n4=elem[1]))