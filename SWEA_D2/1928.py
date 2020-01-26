base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
base64_encoding = dict(enumerate(base64))


def decoNum(x):
    temp = x
    ans = ''
    while temp//2 != 0:
        ans += str(temp % 2)
        temp = temp // 2
    if temp == 1:
        ans += '1'
    ans = ans[::-1]
    return '{0:0>6}'.format(ans)


def bitode(y):
    num = y[::-1]
    result = 0
    for key, bi in dict(enumerate(num)).items():
        if int(bi) == 1:
            result += 2**key
    return result

tcs = int(input())
for t in range(tcs):    
    tc = input()
    decode = []
    for word in tc:
        for key, char in base64_encoding.items():
            if word == char:
                decode.append(key)
    decode_i = ''
    for n in decode:
        decode_i += decoNum(n)
    new_decode = []
    for k in range(0, len(decode_i), 8):
        new_decode.append(decode_i[k:k+8])
    new_string = ''
    for w in new_decode:
        new_string += chr(bitode(w))
    print(f'#{t+1} {new_string}')