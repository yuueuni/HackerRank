N = int(input())
scores = list(map(int, input().split()))

sort_scores = sorted(scores)
median = N/2
print(sort_scores[int(median)])