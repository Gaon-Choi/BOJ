text=input()
text=text.split()
for x in range(len(text)):
    text[x]=int(text[x])
j=0
b=0
while j<=len(text)-2:
    if text[j]<=text[j+1]:
        j+=1
        b+=1
    else: j+=1
if b==len(text)-1:
    print("Good")
else: print("Bad")
