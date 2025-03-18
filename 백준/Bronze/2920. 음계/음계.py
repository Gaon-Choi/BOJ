line = input()
lists = list(map(int, line.split()))

desc = True; asc = True;
for i in range(len(lists)-1):
    if lists[i] > lists[i+1]: asc = False
    if lists[i] < lists[i+1]:desc = False
if asc is True and desc is False:
    print('ascending')
elif asc is False and desc is True:
    print('descending')
else:
    print('mixed')