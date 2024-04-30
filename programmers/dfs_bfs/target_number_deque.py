from collections import deque

# numbers target return
inputs = [
[[1, 1, 1, 1, 1], '3 5'],
[[4, 1, 2, 1], '4 2']
]


def solution(numbers, target):
    answer = 0
    # 각 숫자 +, - 로 케이스 확인
    dq = deque()
    dq.append((numbers[0], 0))
    dq.append((-1 * numbers[0], 0))
    length = len(numbers)
    while dq:
        num, idx = dq.popleft()
        idx += 1
        if idx < length:
            dq.append((num + numbers[idx], idx))
            dq.append((num - numbers[idx], idx))
        else:
            if num == target:
                answer += 1
    return answer


if __name__ == "__main__":
    for inp in inputs:
        numbers = inp[0]
        target, result = map(int, inp[1].split())
        res = solution(numbers, target)
        print(res, result)