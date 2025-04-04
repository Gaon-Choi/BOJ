const_score_weight = [1, 2, 4, 8]

def rotate(idx, d):
    # 시계 방향
    if d == 1:
        elem = gear[idx].pop()
        gear[idx] = [elem] + gear[idx]
    else:
        elem = gear[idx].pop(0)
        gear[idx] = gear[idx] + [elem]

def get_rotation_directions(start, direction):
    directions = [0] * 4
    directions[start] = direction

    # 왼쪽 톱니 확인
    for i in range(start - 1, -1, -1):
        if gear[i][2] != gear[i + 1][6]:
            directions[i] = -directions[i + 1]
        else:
            break

    # 오른쪽 톱니 확인
    for i in range(start + 1, 4):
        if gear[i - 1][2] != gear[i][6]:
            directions[i] = -directions[i - 1]
        else:
            break

    return directions
    

gear = []

for _ in range(4):
    gear.append(list(map(int, list(input()))))

k = int(input())

moves = []

for _ in range(k):
    moves.append(list(map(int, input().split())))

for move in moves:
    table_no, direction = move
    table_no -= 1

    direction_arr = get_rotation_directions(table_no, direction)

    for i in range(4):
        if direction_arr[i] != 0:
            rotate(i, direction_arr[i])

    #rotate_recursive(table_no, direction, 1, 2)

    # rotate_left_table = False
    # rotate_right_table = False

    # if table_no - 1 >= 0 and gear[table_no - 1][2] != gear[table_no][6]:
    #     rotate_left_table = True

    # if table_no + 1 < 4 and gear[table_no + 1][6] != gear[table_no][2]:
    #     rotate_right_table = True

    # # 현재 테이블 회전
    # rotate(table_no, direction)

    # # 양쪽 테이블 회전
    # if rotate_left_table:
    #     rotate(table_no - 1, -direction)

    # if rotate_right_table:
    #     rotate(table_no + 1, -direction)

total_score = 0

for i in range(4):
    total_score += gear[i][0] * const_score_weight[i]

print(total_score)

