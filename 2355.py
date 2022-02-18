def medium(a, b): return (a+b)/2
def nums(a, b): return b - a + 1
a, b = map(int, (input()).split())
if a <= b: print(int(medium(a, b)*nums(a, b)))
else: print(int(medium(a, b)*nums(b, a)))