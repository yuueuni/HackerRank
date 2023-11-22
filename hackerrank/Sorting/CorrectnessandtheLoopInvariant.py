def insertion_sort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


# m = int(input().strip())
# ar = [int(i) for i in input().strip().split()]
m = 6
ar = [7, 4, 3, 5, 6, 2]

insertion_sort(ar)
print(" ".join(map(str, ar)))
