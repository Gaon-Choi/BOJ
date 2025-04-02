import math

d, h, w = map(int, input().split())
ratio = math.sqrt(d ** 2 // (h ** 2 + w ** 2))

ratio_h = int(math.sqrt(d ** 2 * (h ** 2) / (h ** 2 + w ** 2)))
ratio_w = int(math.sqrt(d ** 2 * (w ** 2) / (h ** 2 + w ** 2)))

print(ratio_h, ratio_w)