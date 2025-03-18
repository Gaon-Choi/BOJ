s, k, h = map(int, input().split())

if (s + k + h >= 100):
    print("OK")
else:
    maxima = min(s, k, h)
    if maxima == s:
        print("Soongsil")
    elif maxima == k:
        print("Korea")
    else:
        print("Hanyang")