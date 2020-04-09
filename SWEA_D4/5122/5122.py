import sys

sys.stdin = open('input.txt')

T = int(input())


class Node():
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node

        self.before = None
        self.current = None

    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node

    def move(self, d):
        self.current = self.head.link
        self.before = self.head
        for _ in range(d):
            if self.current == None:
                return False
            self.before = self.current
            self.current = self.current.link
        return True
    
    def insert(self, idx, data):
        new_node = Node(data)
        self.move(idx)
        self.before.link = new_node
        new_node.link = self.current

    def delete(self, idx):
        self.move(idx)
        self.before.link = self.current.link
    
    def change(self, idx, data):
        self.move(idx)
        self.current.data = data
    
    def result(self, idx):
        if self.move(idx):
            return self.current.data
        else:
            return -1


for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    seq = LinkedList()
    
    for i in map(int, input().split()):
        seq.append(i)
    
    for _ in range(m):
        data = list(input().split())
        if data[0] == 'I':
            seq.insert(int(data[1]), int(data[2]))
        elif data[0] == 'D':
            seq.delete(int(data[1]))
        elif data[0] == 'C':
            seq.change(int(data[1]), int(data[2]))
    print(f'#{tc} {seq.result(l)}')