# tickets, result
from copy import deepcopy

inputs = [
    [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], ["ICN", "JFK", "HND", "IAD"]],
    [[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]], ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]],
    [[["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]], ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]]
]


def solution(tickets):
    def dfs(current, path, used_tickets):
        if len(path) == len(tickets) + 1:  # 모든 티켓을 사용한 경우
            return path

        for i, ticket in enumerate(tickets):
            if ticket[0] == current and not used_tickets[i]:
                next_city = ticket[1]
                used_tickets[i] = True
                result = dfs(next_city, path + [next_city], used_tickets)
                if result:
                    return result
                used_tickets[i] = False  # 다른 경로를 탐색하기 위해 마킹을 취소

    tickets.sort()  # 알파벳 순으로 탐색하기 위해 정렬
    used_tickets = [False] * len(tickets)  # 티켓 사용 여부를 나타내는 리스트
    answer = dfs("ICN", ["ICN"], used_tickets)
    return answer


if __name__ == "__main__":
    for inp in inputs:
        tickets, result = inp[0], inp[1]
        res = solution(tickets)
        print(res == result, res, result)
