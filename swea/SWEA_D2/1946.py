tc = int(input())
for t in range(tc):
    n = int(input())
    doc = {}
    for i in range(n):
        key, value = input().split()
        doc[key] = int(value)
    origin_doc = ''
    for key, value in doc.items():
        origin_doc += key*value
    print('#{}'.format(t+1))
    for k in range(0, len(origin_doc),10):
        print(origin_doc[k:k+10])