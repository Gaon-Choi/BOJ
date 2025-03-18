resistor = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

a = resistor.index(input())
b = resistor.index(input())
c = resistor.index(input())

print(int(str(a) + str(b)) * (10 ** c))