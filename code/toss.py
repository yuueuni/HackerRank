# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solve(scores):
	avg = sum(scores)/len(scores)
	if avg >= 90:
		grade = 'A'
	elif avg >= 80:
		grade = 'B'
	elif avg >= 70:
		grade = 'C'
	elif avg >= 60:
		grade = 'D'
	else:
		grade = 'F'
	return avg, grade


input_list = list(map(int, input().split()))
average, grade = solve(input_list)
print(format(average, ".2f"), grade)

# ------------------------------
"""
select team, sum(score)
from records
where score >= 30 and team = "동팀"
"""