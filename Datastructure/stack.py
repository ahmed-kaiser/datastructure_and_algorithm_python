# ----- Implementation of Stack Data structure ----
class Stack:
    def __init__(self):
        self.sList = []
        self.Top = -1

    # # adds item to top of the stack
    def push(self, item):
        self.Top += 1
        self.sList.append(item)

    # returns item from top of the stack
    def pop(self):
        self.Top -= 1
        return self.sList.pop()

    def isEmpty(self):
        return self.Top == -1

    def size(self):
        return self.Top

    def top(self):
        return self.sList[self.Top]

if __name__ == '__main__':
    n = Stack()
    n.push(6)
    n.push(3)
    n.push(10)
    n.push(7)
    n.pop()

    print(n.isEmpty())
    print(n.size())
    print(n.top())