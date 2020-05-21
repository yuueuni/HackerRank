from collections import deque

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    nums = deque()
    check = [0]*1000001
    nums.append(n)
    while nums:
        cur = nums.popleft()
        if cur == m:
            cnt = check[m]
            break
        else:
            data = [cur+1, cur-1, cur*2, cur-10]
            for d in data:
                if 0 <= d <= 1000000 and not check[d]:
                    nums.append(d)
                    check[d] = check[cur] +1
    print(f'#{tc} {cnt}')