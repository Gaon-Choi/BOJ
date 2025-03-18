ans = list()

num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    ans.append(a+b)
for i in range(len(ans)):
    print("Case %d: %d" % (i + 1, ans[i]))