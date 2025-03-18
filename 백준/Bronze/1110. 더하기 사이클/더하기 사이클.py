def transform_number(n: int):
    n_str = str(n)
    
    if n < 10:
        n_str = "0" + n_str
    first = n_str[-1]
    temp = 0
    for c in n_str:
        temp += int(c)
    second = str(temp)[-1]
    return int(first + second)

origin_num = int(input())
num = origin_num

answer = 0

while True:
	num = transform_number(num)
	answer += 1
	if num == origin_num:
	    break

print(answer)