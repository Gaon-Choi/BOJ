n = int(input())

friends = dict()

arr = input().split()

for elem in arr:
    friends[elem] = 0

for _ in range(n):
    arr2 = input().split()

    for elem in arr2:
        friends[elem] += 1

friends_list = list(friends.items())
friends_list.sort(key = lambda x : (-x[1], x[0]))

for k, v in friends_list:
    print(k, v)