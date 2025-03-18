text = input()

result = ""

isOpen = False
temp = ""

for c in text:
    if c == "<":
        isOpen = True
        result += temp[-1::-1]
        result += "<"
        temp = ""
        continue
    elif c == ">":
        isOpen = False
        result += temp
        result += ">"
        temp = ""
        continue
    elif c == " ":
        if isOpen:
            result += temp
        else:
            result += temp[-1::-1]
        result += " "
        temp = ""
        continue
    
    temp += c

if len(temp) > 0:
    result += temp if isOpen else temp[-1::-1]

print(result)