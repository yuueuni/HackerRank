import time
from typing import List

"""
핸드폰 키패드로 만들 수 있는 문자열 구하기
"""


class Solution:
    keypad = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    def solution(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in self.keypad[int(digits[i])]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        result = []
        dfs(0, "")
        return result


if __name__ == '__main__':
    start = time.time()
    result = Solution().solution("23")
    end = time.time()
    print(result, end - start)
