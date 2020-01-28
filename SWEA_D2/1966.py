
tc = int(input())
for t in range(tc):
    N = int(input())
    word = list(map(int, input().split()))
    result = sorted(word)
    print('#{}'.format(t+1), ' '.join(map(str, result)))