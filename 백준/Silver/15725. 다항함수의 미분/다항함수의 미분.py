expr = input()
temp = []
result = []

for i in range(len(expr)):
    if (expr[i] == "+" or expr[i] == "-") and i != 0:
        temp.append(expr[:i])
        expr = expr[i:]
        break

temp.append(expr)

for elem in temp:
	deg = elem.count('x')
	if 'x' in elem:
	    coee = elem[0:elem.index('x')]
	    coeff = 1 if coee == "" else -1 if coee == "-" else int(coee)
	    new_coeff = coeff * deg
	    result.append(("-" if new_coeff == -1 else "") + (str(new_coeff) if abs(new_coeff) != 1 else "") + ('x' * (deg - 1) if abs(new_coeff) != 1 else "1"))

if len(result) == 0:
    result.append('0')

print("".join(result), sep="")