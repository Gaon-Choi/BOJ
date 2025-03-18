rest = int(input())
rest = 1000 - rest

total = 0
total += (rest // 500)
rest -= (rest // 500) * 500

total += (rest // 100)
rest -= (rest // 100) * 100

total += (rest // 50)
rest -= (rest // 50) * 50

total += (rest // 10)
rest -= (rest // 10) * 10

total += (rest // 5)
rest -= (rest // 5) * 5

total += rest

print(total)