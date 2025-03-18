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
	    coeff = int(elem[0:elem.index('x')])
	    new_coeff = coeff // (deg + 1)
	    result.append(("-" if new_coeff == -1 else "") + (str(new_coeff) if abs(new_coeff) != 1 else "") + ('x' * (deg + 1)))
	else:
	    if elem == '+1':
	        result.append('+x')
	    elif elem == '-1':
	        result.append('-x')
	    elif elem == '0':
	        print("W")
	        exit(0)
	    elif elem == "1":
	        result.append('x')
	    elif elem == '+0' or elem == '-0':
	        continue
	    else:
	        result.append(str(elem) + 'x')

print("".join(result) + "+W", sep="")