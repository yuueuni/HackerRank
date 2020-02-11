dama_num = int(input())
dama_list = list(map(int, input().split()))
st_num = int(input())
​
def turn(number):
    if number == 1 :
        return 0
    elif number == 0 :
        return 1
​
for _ in range(st_num):
    s, n = map(int, input().split())
​
    if s == 1:
        for i in range(dama_num):
            if (i+1) % n == 0 :
                dama_list[i] = turn(dama_list[i])
​
    elif s == 2:
        dama_list[n-1] = turn(dama_list[n-1])
​
        for j in range(1, min(n, dama_num-n+1)):
            if dama_list[n-1-j] == dama_list[n-1+j]:
                dama_list[n-1-j] = turn(dama_list[n-1-j])
                dama_list[n-1+j] = turn(dama_list[n-1+j])
            else:
                break
​
for n in range(dama_num):
    print(dama_list[n],end=' ')
    if (n+1) % 20 == 0:
        print('')