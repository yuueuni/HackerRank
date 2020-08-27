def solution(genres, plays):
    answer = []
    gpDict = {genre:[] for genre in set(genres)}
    for gp in zip(genres, plays, range(len(genres))):
        gpDict[gp[0]].append([gp[1], gp[2]])
    gpSort = sorted(list(gpDict.keys()), key=lambda x: sum(map(lambda y: y[0], gpDict[x])), reverse = True)
    print(gpDict)
    print(gpSort)
    answer = list(map(lambda x: x[1], gpDict[s] for s in gpSort))
    return answer