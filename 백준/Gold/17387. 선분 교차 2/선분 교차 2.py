import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    # CCW (Counter Clock Wise)
    # 3개의 점 A, B, C가 있을 때, 이 점들을 잇는 선의 방향을 구하는 알고리즘

    p1x, p1y = p1
    p2x, p2y = p2
    p3x, p3y = p3

    return (p2x - p1x) * (p3y - p1y) - (p2y - p1y) * (p3x - p1x)

def is_intersect(line1, line2):
    p1, p2 = line1
    p3, p4 = line2

    ab = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    cd = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    if (ab <= 0 and cd <= 0):
        # 두 선분이 일직선상에 위치하는 경우
        # 한 점이 한 선분 위에 포개어져 있는지 확인
        if ab == 0 and cd == 0:
            return  min(p1[0], p2[0]) <= max(p3[0], p4[0]) \
            and     min(p3[0], p4[0]) <= max(p1[0], p2[0]) \
            and     min(p1[1], p2[1]) <= max(p3[1], p4[1]) \
            and     min(p3[1], p4[1]) <= max(p1[1], p2[1])
            
        return True
    
    return False

line1 = []
line2 = []

x0, y0, x1, y1 = map(int, input().split())
line1.extend([[x0, y0], [x1, y1]])
x0, y0, x1, y1 = map(int, input().split())
line2.extend([[x0, y0], [x1, y1]])

print(1 if is_intersect(line1, line2) else 0)
