text = '9780921418'

for _ in range(3):
    text += input()
    
total = 0

for idx, v in enumerate(text):
    total += (1 if idx % 2 == 0 else 3) * int(v)
    
print("The 1-3-sum is {total}".format(total=total))