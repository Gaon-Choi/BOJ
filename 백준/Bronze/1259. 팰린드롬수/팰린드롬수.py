answer = []

while True:
    text = input()
    
    if text == '0':
        break
    
    if text == text[-1::-1]:
        answer.append(True)
    else:
        answer.append(False)

for elem in answer:
    print("yes" if elem else "no")