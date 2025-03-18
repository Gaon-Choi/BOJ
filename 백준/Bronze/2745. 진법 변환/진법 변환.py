number, base = input().split()
base = int(base)

base10 = 0

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i, v in enumerate(list(reversed(number))):
	base10 += (base ** i) * num_list.index(v)

print(base10)