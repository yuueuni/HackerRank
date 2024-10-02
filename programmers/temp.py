def maximize_gold_tickets_dp_unknown_tickets(initial_money, ticket_prices, ticket_sequences):
    from collections import defaultdict

    # DP 테이블을 초기화합니다.
    dp = defaultdict(lambda: 0)
    dp[(initial_money, '')] = 0  # (남은 돈, 가지고 있는 티켓 조합) -> 황금 티켓 개수

    for sequence in ticket_sequences:
        new_dp = defaultdict(lambda: 0)

        for (money, inventory), gold in dp.items():
            # 티켓을 구매하는 경우
            for ticket in sequence:
                price = ticket_prices[ticket]
                if money >= price:
                    new_money = money - price
                    new_inventory = ''.join(sorted(inventory + ticket))  # 새로운 티켓을 추가한 인벤토리
                    new_dp[(new_money, new_inventory)] = max(new_dp[(new_money, new_inventory)], gold + 1)

            # 티켓을 교환하는 경우
            for ticket in sequence:
                count = inventory.count(ticket)
                if count >= 3:
                    price = ticket_prices[ticket]
                    new_money = money + price * (count // 3)  # 티켓을 교환하여 얻은 돈
                    new_inventory = inventory.replace(ticket, '', 3)  # 티켓을 교환한 인벤토리
                    new_dp[(new_money, new_inventory)] = max(new_dp[(new_money, new_inventory)], gold + count // 3)

            new_dp[(money, inventory)] = max(new_dp[(money, inventory)], gold)  # 현재 상태에서 티켓을 사용하지 않는 경우

        dp = new_dp

    # 최종 결과에서 최대 황금 티켓 개수를 찾습니다.
    max_gold_tickets = max(dp.values())
    remaining_money = max([money for (money, _), gold in dp.items() if gold == max_gold_tickets])

    return max_gold_tickets, remaining_money


# 테스트
initial_money = 10
ticket_prices = {'A': 2, 'B': 1}
ticket_sequences = [
    ['A', 'A', 'A'],
    ['A', 'B', 'B'],
    ['A', 'B', 'B'],
    ['A', 'B', 'B']
]

gold_tickets, remaining_money = maximize_gold_tickets_dp_unknown_tickets(initial_money, ticket_prices, ticket_sequences)
print(f"최종 황금 티켓 개수: {gold_tickets}")
print(f"남은 자금: {remaining_money}")
