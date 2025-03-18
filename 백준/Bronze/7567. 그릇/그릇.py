if __name__ == '__main__':
    string = input()
    score = 10
    for i in range(len(string) - 1):
        if (string[i+1] != string[i]):
            score += 10
        else:
            score += 5
    print(score)