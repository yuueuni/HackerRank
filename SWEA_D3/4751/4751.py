import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = list(input())
    temp = word
    ans1 = '.'+'.#..'*len(word)
    ans2 = '.#.#'*len(word)+'.'
    print(ans1)
    print(ans2)
    while temp:
        w = temp.pop(0)
        if len(temp) == 0:
            print('#.'+w+'.#')
        else:
            print('#.'+w+'.', end='')
    print(ans2)
    print(ans1)