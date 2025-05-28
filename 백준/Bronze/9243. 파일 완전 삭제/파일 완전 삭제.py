import sys
input = sys.stdin.readline

n = int(input())

file1 = input().strip()
file2 = input().strip()

if n % 2 == 0:
    print("Deletion succeeded" if file1 == file2 else "Deletion failed")

else:
    flag = True

    for i in range(len(file1)):
        if file1[i] == file2[i]:
            flag = False
            break

    print("Deletion succeeded" if flag else "Deletion failed")
