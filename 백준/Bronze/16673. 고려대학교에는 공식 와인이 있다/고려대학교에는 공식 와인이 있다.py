text=input()
text=text.split()
C=int(text[0]);K=int(text[1]);P=int(text[2])


number=K*C+P*(C**2)
total=0
c=1
while c<=C:
    number_1=K*c+P*(c**2)
    total+=number_1
    c+=1
print(total)