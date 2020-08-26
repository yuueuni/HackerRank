# # My Solution
# Success

def solution(phone_book):
    answer = True
    for p in phone_book:
        t = len(p)
        for c in phone_book:
            if c != p:
                if c[:t] == p:
                    answer = False
                    return answer
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.03ms, 10.7MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.04ms, 10.7MB)
# 테스트 7 〉	통과 (0.04ms, 10.7MB)
# 테스트 8 〉	통과 (0.04ms, 10.7MB)
# 테스트 9 〉	통과 (0.04ms, 10.8MB)
# 테스트 10 〉	통과 (0.03ms, 10.7MB)
# 테스트 11 〉	통과 (0.04ms, 10.6MB)
# 효율성  테스트
# 테스트 1 〉	통과 (1.06ms, 15.2MB)
# 테스트 2 〉	통과 (1.05ms, 15.3MB)
# 채점 결과
# 정확성: 84.6
# 효율성: 15.4
# 합계: 100.0 / 100.0

# -------------------------------------------------------

def solution3(phone_book):
    for i in range(len(phone_book)):
        p = phone_book[i]
        for j in range(i+1, len(phone_book)):
            t = min(len(p), len(phone_book[j]))
            if phone_book[j][:t] == p[:t]:
                return False
    return True
# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.04ms, 10.6MB)
# 테스트 4 〉	통과 (0.03ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.04ms, 10.6MB)
# 테스트 7 〉	통과 (0.04ms, 10.7MB)
# 테스트 8 〉	통과 (0.04ms, 10.8MB)
# 테스트 9 〉	통과 (0.03ms, 10.7MB)
# 테스트 10 〉	통과 (0.04ms, 10.8MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 효율성  테스트
# 테스트 1 〉	통과 (0.18ms, 15.3MB)
# 테스트 2 〉	통과 (0.13ms, 15.3MB)
# 채점 결과
# 정확성: 84.6
# 효율성: 15.4
# 합계: 100.0 / 100.0


# -------------------------------------------------------

def solution2(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True