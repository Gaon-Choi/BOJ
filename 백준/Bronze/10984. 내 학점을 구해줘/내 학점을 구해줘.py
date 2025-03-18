n = int(input())

result = []

for _ in range(n):
    k = int(input())
    
    credit = 0
    tmp_credit = 0
    grade = 0
    
    for _ in range(k):
        tmp = input().split()
        credit += int(tmp[0])
        grade += float(tmp[1]) * int(tmp[0])
        
    result.append([credit, grade / credit])
    
for elem in result:
    print("{total_credit} {total_grade:.1f}".format(total_credit=elem[0], total_grade=elem[1]))