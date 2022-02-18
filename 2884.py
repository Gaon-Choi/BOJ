if __name__ == '__main__':
    hour, minute = (input()).split()
    hour = int(hour); minute = int(minute)
    TIME = hour * 60 + minute
    TIME -= 45
    if TIME < 0: TIME += 1440
    print((TIME // 60), TIME % 60)