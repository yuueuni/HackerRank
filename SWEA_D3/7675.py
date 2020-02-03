t = int(input())

for tc in range(t):
    n = int(input())
    words = list(input().split())
    cnt = idx = 0
    res = [0]*n
    for i in range(len(words)):
        temp = words[i][-1]
        if temp == '.' or temp == '!' or temp == '?':
            word = words[i][:-1]
        else:
            word = words[i]            
        if word[0] == word[0].upper() and word[1:] == word[1:].lower() and word.isalpha():
            cnt += 1
        if temp == '.' or temp == '!' or temp == '?':
            res[idx] = cnt
            idx += 1
            cnt = 0
    print('#{}'.format(tc+1), ' '.join(map(str, res)))