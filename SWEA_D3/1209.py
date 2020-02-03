for tc in range(10):
    n = int(input())
    sample = [ [0]*100 for _ in range(100) ]
    for i in range(100):
        sample[i] = list(map(int, input().split()))
    line = max(sum(sample[i][j] for j in range(100)) for i in range(100))
    ver = max(sum(sample[i][j] for i in range(100)) for j in range(100))
    dia = sum(sample[i][i] for i in range(100))
    rev = sum(sample[i][99-i] for i in range(100))
    print('#{}'.format(tc+1), max(line, ver, dia, rev))