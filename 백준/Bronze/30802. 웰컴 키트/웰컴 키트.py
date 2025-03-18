n = int(input())
s, m, l, xl, xxl, xxxl = map(int, input().split())
t, p = map(int, input().split())

tshirts = 0

for elem in [s, m, l, xl, xxl, xxxl]:
    tshirts += (elem // t) + (1 if elem % t != 0 else 0)
    
print(tshirts)
print(n // p, n % p)