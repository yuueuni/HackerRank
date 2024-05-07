from collections import defaultdict

# nums, result
input = [
    [[3,1,2,3], 2],
    [[3,3,3,2,2,4], 3],
    [[3,3,3,2,2,2], 2]
]


def solution(nums):
    ponketmons = defaultdict(int)
    for num in nums:
        ponketmons[num] += 1
    if len(nums) // 2 >= len(ponketmons.keys()):
        return len(ponketmons.keys())
    else:
        return len(nums) // 2


def solution_2(nums):
    return min(len(nums) / 2, len(set(nums)))


if __name__ == '__main__':
    for d in input:
        nums, result = d[0], d[1]
        res = solution(nums)
        print(result == res, "########", result, res)