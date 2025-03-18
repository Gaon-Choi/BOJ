result = []

for i in range(5):
    name = input()
    if "FBI" in name:
        result.append(i + 1)

if len(result) > 0:
    for elem in result:
        print(elem, end = " ")
else:
    print("HE GOT AWAY!")