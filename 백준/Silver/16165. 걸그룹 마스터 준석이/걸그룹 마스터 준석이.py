import sys
input = sys.stdin.readline

n, m = map(int, input().split())

team_to_idx = dict()
member_to_team = dict()

idx = 0

arr = [[] for _ in range(n)]

for _ in range(n):
    team_name = input().strip()

    team_to_idx[team_name] = idx

    k = int(input())

    for _ in range(k):
        member_name = input().strip()
        member_to_team[member_name] = team_name
        arr[idx].append(member_name)

    idx += 1

for _ in range(m):
    query_name = input().strip()
    query_mode = int(input())

    if query_mode == 1:
        print(member_to_team[query_name])

    else:
        for name in sorted(arr[team_to_idx[query_name]]):
            print(name)