def primeNumber(num):
    prime_list = [2, 3, 5, 7, 11]
    answer = [0]*len(prime_list)
    for i in range(len(prime_list)):
        factor = 0
        prime = prime_list[i]
        while num % prime == 0:
            factor += 1
            num = num // prime
        answer[i] = factor
        if num == 1:
            answer[i] = factor
    return answer


tc= int(input())
for t in range(tc):
    number = int(input())
    result = primeNumber(number)
    print('#{}'.format(t+1), ' '.join(map(str, result)))