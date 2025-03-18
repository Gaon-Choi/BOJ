__ = input()
str1, str2 = __.split()

size = max(len(str1), len(str2))
ans = list()
carry = 0
for i in range(size):
    A = int(str1[-(i + 1)]) if i+1<=len(str1) else 0
    B = int(str2[-(i + 1)]) if i+1<=len(str2) else 0
    m = A+B+carry
    if m>=10: carry=1
    else: carry=0
    ans.append((str(m))[-1])
if str(carry) != "0":
    ans.append(str(carry))
print((''.join(ans))[::-1])
