def primeNumber(num):
    prime_list = []
    answer = {}
    # 소수 판별
    for i in range(2, num+1):
        cnt = 0
        # 소수 리스트 생성
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            prime_list.append(i)
    # 생성된 소수 리스트 이용한 인수 찾기
    for prime in prime_list:
        factor = 0
        while num % prime == 0:
            factor += 1
            num = num // prime
        answer[prime] = factor
        if num == 1:
            break
    return answer

"""
tc = int(input())
for t in range(1, tc+1):
    number = int(input())
    result = primeNumber(number)
    print(result)
"""

result = primeNumber(10)
for k in result.values():
    print(k, end=' ')