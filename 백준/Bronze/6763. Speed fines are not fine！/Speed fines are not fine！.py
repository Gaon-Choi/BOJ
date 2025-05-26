import sys
input = sys.stdin.readline

limit = int(input())
speed = int(input())

diff = speed - limit

if diff <= 0:
    print("Congratulations, you are within the speed limit!")
else:
    fine = -1

    if 1 <= diff <= 20:
        fine = 100
    elif 21 <= diff <= 30:
        fine = 270
    else:
        fine = 500
    
    print(f"You are speeding and your fine is ${fine}.")
