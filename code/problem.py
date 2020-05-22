
# 회전
def rota(data, r):
    n = len(data)
    result = [ [0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-1-i] = data[i][j]
    if r-1 != 0:
        return rota(result, r-1)
    else:
        return result

# sample = [[4, 1, 2], [7, 3, 4], [3, 5, 6]]
# answer = rota(sample, 3)
# print(answer)

# 지뢰찾기
def find(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])

    data = list(list(matrix[x]) for x in range(n))

    result = data
    visited = [ [0]* m for _ in range(n)]

    di = [-1, -1, 20, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    check = [(i, j)]
    if data[i][j] == 'M':
        result[i][j] = 'X'
        return result
    while check:
        i, j = check.pop(0)
        cnt = 0
        for k in range(8):
            ti = i + di[k]
            tj = j + dj[k]
            if 0 <= ti < n and 0 <= tj < m:
                if data[ti][tj] == 'M':
                    cnt += 1
                elif data[ti][tj] == 'E':
                    visited[ti][tj] = 1
                    result[ti][tj] == 'B'
                    check.append((ti, tj))
        if cnt:
            result[i][j] = cnt
        else:
            result[i][j] = 'B'
    return result


# sample = ["EEEEE", "EEMEE", "EEEEE", "EEEEE"]
# answer = find(sample, 2, 0)
# print(answer)


from itertools import permutations

def dic(n, m, k):
    data = '('*n + ')'*m
    permu = list(set(list(permutations(list(data), 4))))
    permu.sort()
    return "".join(permu[k-1])

def sol(n, m, k):
    mylist = []
    result = []
    for i in range(n):
        mylist.append("(")
    for j in range(m):
        mylist.append(")")
    
    mypermutation = permutations(mylist)
    for i in mypermutation:
        result.append(i)
    
    finresult = []
    for i in range(len(result)):
        finresult.append("".join(result[i]))
    answer = list(sorted(set(finresult)))[k-1]
    return answer

answer = dic(2, 2, 5)
print(answer)