factorial = [1, 1]

for i in range(2, 10):
    factorial.append(factorial[-1] * i)

def exp(n):
    result = 0

    for i in range(n + 1):
        result += (1 / factorial[i])

    return result

print("n e")
print("- -----------")

for i in range(10):
    if i <= 1:
        print(i, int(exp(i)))
    elif i == 2:
        print(i, float(exp(i)))
    else:
        print("%d %.9f" % (i, exp(i)))