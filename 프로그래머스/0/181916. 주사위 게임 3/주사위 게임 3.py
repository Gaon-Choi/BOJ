def solution(a, b, c, d):
    if a == b == c == d:
        return 1111 * a
    
    else:
        if a == b == c != d:
            return (10 * a + d) ** 2
        elif a == b == d != c:
            return (10 * a + c) ** 2
        elif a == c == d != b:
            return (10 * a + b) ** 2
        elif b == c == d != a:
            return (10 * b + a) ** 2
        
        else:
            if a == b != c == d:
                return (a + c) * abs(a - c)
            elif a == c != b == d:
                return (a + b) * abs(a - b)
            elif a == d != c == b:
                return (a + c) * abs(a - c)
            else:
                if a == b != c != d:
                    return c * d
                elif b == c != a != d:
                    return a * d
                elif c == d != a != b:
                    return a * b
                elif d == a != b != c:
                    return b * c
                elif a == c != b != d:
                    return b * d
                elif b == d != a != c:
                    return a * c
                else:
                    return min(a, b, c, d)