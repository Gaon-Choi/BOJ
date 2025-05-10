import sys
input = sys.stdin.readline

text = input().strip()

if "N" in text or "n" in text:
    print("Naver D2")
else:
    print("Naver Whale")