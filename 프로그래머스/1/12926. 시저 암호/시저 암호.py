def solution(s, n):
    answer = ''
    
    for c in s:
        if ord('A') <= ord(c) <= ord('Z'):
            answer += chr(ord('A') + (ord(c) + n - ord('A')) % 26)
        elif ord('a') <= ord(c) <= ord('z'):
            answer += chr(ord('a') + (ord(c) + n - ord('a')) % 26)
        else:
            answer += c
    
    return answer