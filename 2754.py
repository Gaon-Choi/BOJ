grade = input()
if grade == 'F': ans=0
else:
    if grade[0]=='A': ans=4
    elif grade[0]=='B': ans=3
    elif grade[0]=='C': ans=2
    elif grade[0]=='D': ans=1

    if grade[1]=='+': ans+=0.3
    elif grade[1]=='-': ans-=0.3

print("{:.1f}".format(ans))