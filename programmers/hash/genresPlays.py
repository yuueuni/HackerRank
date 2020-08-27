
# - Success

def solution(genres, plays):
    answer = []
    gpDict = {genre:[] for genre in set(genres)}
    for gp in zip(genres, plays, range(len(genres))):
        gpDict[gp[0]].append([gp[1], gp[2]])
    gpSort = sorted(list(gpDict.keys()), key=lambda x: sum(map(lambda y: y[0], gpDict[x])), reverse = True)
    for g in gpSort:
        gpSortP = [gp[1] for gp in sorted(gpDict[g], key=lambda x: (x[0], -x[1]), reverse = True)]
        answer += gpSortP[:2]
    return answer

# ------------------------------------------------------------------------------------------------------------------------

# - Other Soultion

def solution2(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer