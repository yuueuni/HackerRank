import time
"""
두 수의 합
- 주어진 합이 되는 인덱스 리턴
"""


def two_sum1(target: int, numbers: list[int]) -> list[int]:
    for i in range(len(numbers)):
        answer = [j for j in range(len(numbers)) if numbers[i] + numbers[j] == target]
        if answer:
            answer.append(i)
            return sorted(answer)


def two_sum2(target: int, numbers: list[int]) -> list[int]:
    for i, n in enumerate(numbers):
        complement = target - n
        if complement in numbers[i+1:]:
            return [numbers.index(n), numbers[i+1:].index(complement) + (i + 1)]


def two_sum3(target: int, numbers: list[int]) -> list[int]:
    num_map = {}
    for i, n in enumerate(numbers):
        num_map[n] = i

    for index, number in enumerate(numbers):
        if target - number in num_map and i != num_map[target - number]:
            return [numbers.index(number), num_map[target - number]]


def two_sum4(target: int, numbers: list[int]) -> list[int]:
    num_map = {}
    for index, number in enumerate(numbers):
        if target - number in num_map and index != num_map[target - number]:
            return [num_map[target - number], index]
        num_map[number] = index


def two_sum5(target: int, numbers: list[int]) -> list[int]:
    left, right = 0, len(numbers) - 1
    numbers.sort()
    while left != right:
        temp_sum = numbers[left] + numbers[right]
        if temp_sum < target:
            left += 1
        elif temp_sum > target:
            right -= 1
        else:
            return [left, right]


if __name__ == '__main__':
    target = 9
    numbers = [2, 7, 11, 15]
    start = time.time()
    result = two_sum5(target, numbers)
    end = time.time()
    print(result, end - start)