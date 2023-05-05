tc = int(input())
for t in range(tc):
    n, k = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'F']
    scores = {}
    for i in range(n):
        # mid 0.35 , final 0.45 , task 0.20
        mid, final, task = map(int, input().split())
        scores[i+1] = round(mid*0.35 + final*0.45 + task*0.2, 2)
    temp = sorted(scores.values(), reverse=True)
    k_rank = temp.index(scores[k])
    k_grade = grade[ int(k_rank/ (n/10 )) ]
    print('#{}'.format(t+1), k_grade)