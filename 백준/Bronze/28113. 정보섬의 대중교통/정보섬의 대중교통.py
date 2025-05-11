import sys
input = sys.stdin.readline

n, bus, subway = map(int, input().split())

subway_time = max(n, subway)

if subway_time > bus:
    print("Bus")
elif subway_time == bus:
    print("Anything")
else:
    print("Subway")