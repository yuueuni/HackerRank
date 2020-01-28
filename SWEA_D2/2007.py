def test(w):
    for i in range(1, len(w)):
        if w[:i] == w[i:2*i]:
            ans = len(w[:i])
            break
    return ans


tc = int(input())
for t in range(tc):
    test_case = input()
    result = test(test_case)
    print('#{}'.format(t+1), result)