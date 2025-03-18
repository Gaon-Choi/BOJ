x = []
y = []

for _ in range(3):
    x_, y_ = map(int, input().split())
    
    if x_ in x:
        x.remove(x_)
    else:
        x.append(x_)
        
    if y_ in y:
        y.remove(y_)
    else:
        y.append(y_)
        
print(x[0], y[0])