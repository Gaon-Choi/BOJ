import sys
input = sys.stdin.readline

n = int(input())

mySet = [False] * 21

def add(x):
    mySet[x] = True
        
def remove(x):
    mySet[x] = False
        
def check(x):
    return mySet[x]
    
def toggle(x):
    mySet[x] = not mySet[x]
        
def S():
    return [True] * 21
    
def empty():
    return [False] * 21
    
for _ in range(n):
    op = input().split()
    
    operation = op[0]
        
    if operation == "empty":
        mySet = empty()
    elif operation == "all":
        mySet = S()
    else:
        val = int(op[1])
        
        if operation == "add":
            add(val)
        elif operation == "check":
            print(1 if check(val) else 0)
        elif operation == "remove":
            remove(val)
        elif operation == "toggle":
            toggle(val)