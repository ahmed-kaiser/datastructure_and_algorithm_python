# ------- Implementation of Queue Data Structure ---------
class Queue:
    def __init__(self):
        self.dList = []

    # adds item to end of the queue
    def enQueue(self, item):
        self.dList.append(item)

    # removes and returns item from font of the queue
    def deQueue(self):
        return self.dList.pop(0)

    # returns font value from queue
    def peek(self):
        return self.dList[0]

    def isEmpty(self):
        return len(self.dList) == 0

    def size(self):
        return len(self.dList)


if __name__ == '__main__':
    q = Queue()
    q.enQueue(4)
    q.enQueue(12)
    q.enQueue(9)
    q.enQueue(7)

    print(q.deQueue())
    print(q.peek())
    print(q.isEmpty())


    