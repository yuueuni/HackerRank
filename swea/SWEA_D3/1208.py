for t in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
    while dump:
        max_b = box.index(max(box))
        min_b = box.index(min(box))
        box[max_b] -= 1
        box[min_b] += 1
        dump -= 1
    print('#{}'.format(t+1), max(box)-min(box))
        