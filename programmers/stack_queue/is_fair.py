# s     	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false

def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    check = []
    for e in s:
        if e == '(':
            check.append(e)
        else:
            if not check or check[-1] == e:
                return False
            check.pop()
    return True if not check else False
