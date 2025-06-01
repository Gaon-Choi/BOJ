import sys
input = sys.stdin.readline

HOUR, MINUTE = 3600, 60

for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    total = (eh * HOUR + em * MINUTE + es) - (sh * HOUR + sm * MINUTE + ss)

    print(total // HOUR, (total % HOUR) // MINUTE, total % MINUTE)
