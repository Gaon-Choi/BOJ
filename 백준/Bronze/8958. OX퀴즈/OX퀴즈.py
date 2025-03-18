def decide(text):
    length=len(text)
    text_1=list(text) #데이터를 글자별로 쪼갬
    score=0
    score_1=0
    for x in range(0, length):
        if text_1[x]=='O':
            score_1+=1
            score+=score_1
        else:
            score_1=0
    print(score)

#Main
a=int(input()) #케이스의 개수
string=[]      #케이스의 데이터가 저장되는 곳
for z in range(0,a):
    input_data=input()
    string.append(input_data)
for y in range(0, a):
    decide(string[y])