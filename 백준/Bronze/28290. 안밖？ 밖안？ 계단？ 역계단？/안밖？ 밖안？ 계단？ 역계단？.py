import sys
input = sys.stdin.readline

word = input().strip()

if word in {"fdsajkl;", "jkl;fdsa"}:
    print("in-out")
elif word in {"asdf;lkj", ";lkjasdf"}:
    print("out-in")
elif word == "asdfjkl;":
    print("stairs")
elif word == ";lkjfdsa":
    print("reverse")
else:
    print("molu")