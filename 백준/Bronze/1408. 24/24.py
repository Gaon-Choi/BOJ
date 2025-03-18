time_from = input()
h1, m1, s1 = map(int, time_from.split(':'))

time_to = input()
h2, m2, s2 = map(int, time_to.split(':'))

rest = (3600 * h2 + 60 * m2 + s2) - (3600 * h1 + 60 * m1 + s1)
if rest < 0: rest += 24 * 60 * 60
H = rest // 3600
M = (rest % 3600) // 60
S = (rest % 3600) % 60

print("%02d:%02d:%02d" % (H, M, S))