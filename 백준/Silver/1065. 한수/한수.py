def hansu(number:int):
    number = str(number)
    if len(number) == 1:
        return True
    flag = True
    leng = int(number[0])-int(number[1])
    for i in range(len(number)-1):
        if leng != int(number[i])-int(number[i+1]):
            flag = False
    return flag

count = 0
maxi = int(input())
for i in range(1, maxi + 1):
    if hansu(i):
        count +=1
print(count)