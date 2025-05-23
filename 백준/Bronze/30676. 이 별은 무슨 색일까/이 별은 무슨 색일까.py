import sys
input = sys.stdin.readline

freq = int(input())

frequency_list = [
    (425, "Violet"),
    (450, "Indigo"),
    (495, "Blue"),
    (570, "Green"),
    (590, "Yellow"),
    (620, "Orange"),
    (781, "Red"),
]

for f, color in frequency_list:
    if freq < f:
        print(color)
        break