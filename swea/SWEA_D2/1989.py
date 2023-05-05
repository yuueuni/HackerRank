def test(w):
    temp = w[::-1]
    if temp == w:
        return 1
    else:
        return 0

tc = int(input())
for t in range(tc):
    word = input()
    result = test(word)
    print('#{}'.format(t+1), result)