def is_acceptable(text):
    cnt = 0
    is_vowel = False
    has_aeiou = False
    prev = ''

    for c in text:
        if prev == c and c not in {'e', 'o'}:
            return False
        
        if c in {'a', 'e', 'i', 'o', 'u'}:
            has_aeiou = True

            if is_vowel:
                cnt += 1
                if cnt == 3:
                    return False
            else:
                is_vowel = True
                cnt = 1

        else:
            if is_vowel:
                is_vowel = False
                cnt = 1
            else:
                cnt += 1
                if cnt == 3:
                    return False
                
        prev = c

    return has_aeiou

while True:
    text = input().strip()

    if text == "end":
        break

    if is_acceptable(text):
        print(f"<{text}> is acceptable.")
    else:
        print(f"<{text}> is not acceptable.")
