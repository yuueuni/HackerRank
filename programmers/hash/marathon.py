# 효율성 fail

def solution(participant, completion):
    answer = []
    for person in participant:
        if person not in answer:
            completion_person = completion.count(person)
            participant_person = participant.count(person)
            count_person = participant_person - completion_person
            for _ in range(count_person):
                answer.append(person)
    return ','.join(answer)

# -------------------------------------------------------------------

# Success
import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# -------------------------------------------------------------------

# # My Solution
# Success

def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]