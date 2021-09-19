class Node:
    def __init__(self, value):
        self.nodeValue = value
        self.nextNode = None

class LinkedList:
    def __init__(self, value=None):
        self.head = value


    def append(self, value):
        new_node = Node(value)
        current_node = self.head

        while current_node:
            if current_node.nextNode is None:
                current_node.nextNode = new_node
                break
            else:
                current_node = current_node.nextNode
        else:
            self.head = new_node


    def insert(self, item, pos):
        new_node = Node(item)
        current_node = self.head
        if pos == 0:
            if current_node is None:
                current_node = new_node
            else:
                self.head = new_node
                new_node.nextNode = current_node

        elif pos > self.size():
            print('Index out of range')

        elif pos == self.size():
            self.append(item)

        else:
            index = 0
            previous_node = None
            while current_node:
                if index != pos:
                    previous_node = current_node
                    current_node = current_node.nextNode
                    index += 1
                else:
                    previous_node.nextNode = new_node
                    new_node.nextNode = current_node
                    break


    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


    def size(self):
        count = 0
        if self.head is None:
            return count
        else:
            current_node = self.head
            while current_node:
                count += 1
                current_node = current_node.nextNode
            return count


    def index(self, item):
        index = 0
        found = False
        current_node = self.head
        while current_node.nextNode != None and not found:
            if current_node.nodeValue == item:
                found = True
                return index
            else:
                current_node = current_node.nextNode
                index += 1

        if found is False:
            return 'Item not in list'

    
    def search(self, item):
        found = False
        current_node = self.head
        while current_node:
            if current_node.nodeValue == item:
                found = True
                return found
            else:
                current_node = current_node.nextNode

        if found is False:
            return 'Item not in list'


    def remove(self, item):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.nodeValue == item:
                previous_node.nextNode = current_node.nextNode
                break
            else:
                previous_node = current_node
                current_node = current_node.nextNode


    def pop(self):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.nextNode is None:
                previous_node.nextNode = None
                return current_node.nodeValue
            else:
                previous_node = current_node
                current_node = current_node.nextNode


    # ---- Iterative way to make the list in reverse order -------
    def reverse(self):
        current_node = self.head
        previous_node = None
        next_node = current_node.nextNode

        while current_node:
            if previous_node is None:
                current_node.nextNode, previous_node = previous_node, current_node
                current_node = next_node

            elif previous_node and current_node.nextNode is not None:
                next_node = current_node.nextNode
                current_node.nextNode, previous_node = previous_node, current_node
                current_node = next_node

            elif current_node.nextNode is None:
                current_node.nextNode, previous_node = previous_node, current_node
                self.head = current_node
                return


    # ---- Recursive way to make the list in reverse order -------
    # take 'head node' as parameter
    def reverseList(self, node):
        if node.nextNode is None:
            self.head = node
            return

        self.reverseList(node.nextNode)
        current_node = node
        next_node = current_node.nextNode
        current_node.nextNode, next_node.nextNode = None, current_node 


    # ---- Iterative way to print the list -------
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.nodeValue, end='  ')
            current_node = current_node.nextNode
        print('')


    # ---- Recursive way to print the list in forward order -------
    # take 'head node' as parameter
    def forwardPrintList(self, node):
        if node is None:
            return
        print(node.nodeValue, end='  ')
        self.forwardPrintList(node.nextNode)


    # ---- Recursive way to print the list in reverse order -------
    # take 'head node' as parameter
    def reversePrintList(self, node):
        if node is None:
            return       
        self.reversePrintList(node.nextNode)
        print(node.nodeValue, end='  ')


    def get_head(self):
        return self.head




if __name__ == '__main__':
    l = LinkedList()

    # print(l.is_empty())

    l.append(6)
    l.append(9)
    l.insert(7, 1)
    l.append(3)
    l.insert(5, 4)

    # print(l.is_empty())
    # l.printList()
    # print(l.size())
    # print(l.index(3))
    # print(l.search(5))
    # l.remove(5)
    # l.printList()
    # print(l.pop())
    # l.printList()
    # l.reverse()
    # l.printList()
    # l.printList(l.get_head())
    # l.reversePrintList(l.get_head())
    # l.printList()
    # l.reverseList(l.get_head())
    l.printList()
