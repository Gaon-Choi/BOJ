import sys
input = sys.stdin.readline

n = int(input())

fruit_dict = dict()

for _ in range(n):
    fruit, num = input().strip().split()
    num = int(num)

    if fruit in fruit_dict:
        fruit_dict[fruit] += num
    else:
        fruit_dict[fruit] = num

flag = False

for k, v in list(fruit_dict.items()):
    if v == 5:
        flag = True
        break

print("YES" if flag else "NO")
