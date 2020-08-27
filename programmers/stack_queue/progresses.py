
# Old My Solution
# - Success

import math

def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    front = 0
    for idx in range(len(progresses)):
        if progresses[front] < progresses[idx]:
            answer.append(idx-front)
            front = idx
    answer.append(len(progresses)-front)
    return answer

# 테스트 1 〉	통과 (0.05ms, 10.7MB)
# 테스트 2 〉	통과 (0.08ms, 10.7MB)
# 테스트 3 〉	통과 (0.07ms, 10.7MB)
# 테스트 4 〉	통과 (0.06ms, 10.7MB)
# 테스트 5 〉	통과 (0.05ms, 10.7MB)
# 테스트 6 〉	통과 (0.05ms, 10.7MB)
# 테스트 7 〉	통과 (0.07ms, 10.8MB)
# 테스트 8 〉	통과 (0.05ms, 10.7MB)
# 테스트 9 〉	통과 (0.06ms, 10.7MB)
# 테스트 10 〉통과 (0.07ms, 10.8MB)
# 테스트 11 〉통과 (0.05ms, 10.6MB)

# ----------------------------------------------------------------------------------------

# - My Solution
# - Success

def solution2(progresses, speeds):
    answer = []
    finish = 0
    work = list(map(lambda x, y: x + y, progresses, speeds))
    while work:
        if work[0] >= 100:
            work.pop(0)
            speeds.pop(0)
            finish += 1
        else:
            if finish:
                answer.append(finish)
                finish = 0
            work = list(map(lambda x, y: x + y, work, speeds))
    answer.append(finish)
    return answer

# 테스트 1 〉	통과 (0.05ms, 10.7MB)
# 테스트 2 〉	통과 (0.36ms, 10.6MB)
# 테스트 3 〉	통과 (0.48ms, 10.8MB)
# 테스트 4 〉	통과 (0.21ms, 10.6MB)
# 테스트 5 〉	통과 (0.05ms, 10.7MB)
# 테스트 6 〉	통과 (0.08ms, 10.8MB)
# 테스트 7 〉	통과 (0.43ms, 10.6MB)
# 테스트 8 〉	통과 (0.09ms, 10.7MB)
# 테스트 9 〉	통과 (0.32ms, 10.8MB)
# 테스트 10 〉통과 (0.34ms, 10.7MB)
# 테스트 11 〉통과 (0.05ms, 10.7MB)