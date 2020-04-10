import sys

sys.stdin = open('input.txt')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        head = Node('head')
        self.head = head
        self.tail = head

        self.before = None
        self.current = None

        self.num_of_data = 0
    
    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node
        self.tail.link = self.head.link
        self.num_of_data += 1
    
    def first(self):
        self.current = self.head.link
        self.before = self.tail
        return self.current.data
    
    def next(self):
        self.before = self.current
        self.current = self.current.link
        return self.current.data
    
    def insert(self, data):
        new_node = Node(data)
        self.before.link = new_node
        new_node.link = self.current
        self.current = new_node
        self.num_of_data += 1
    
    def func(self, c):
        for _ in range(c):
            self.next()
        num = self.before.data + self.current.data
        self.insert(num)

    def result(self):
        result = [self.first()]
        for _ in range(self.num_of_data-1):
            result.append(self.next())
        return ' '.join(map(str, result[-1:-11:-1]))


T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    seq = LinkedList()
    for i in map(int, input().split()):
        seq.append(i)
    seq.first()
    for _ in range(k):
        seq.func(m)
    print(f'#{tc} {seq.result()}')