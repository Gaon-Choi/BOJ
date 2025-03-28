n = int(input())
password_dict = dict()

answer = []

for _ in range(n):
    password = input()

    password_dict[password] = 1

    if password[-1::-1] in password_dict:
        answer = [len(password), password[len(password) // 2]]
        break

print(*answer)