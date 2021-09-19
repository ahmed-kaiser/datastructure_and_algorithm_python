# ---------- Doubly linked list -----------
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    
    # insert_at_font function add item at font of the list
    def insert_at_font(self, item):
        node = Node(item)
        if self.head:
            current_node = self.head
            current_node.prevNode = node
            node.nextNode = current_node
            self.head = node
        else:
            self.head = node

        
    # add item in given position
    # if position not given then add data at end of the list
    # here pos hold position data
    def insert(self, item, pos=None):
        node = Node(item)
        current_node = self.head
        index = 0
        if pos == 0:
            self.insert_at_font(item)
        
        elif pos is None:
           while current_node:
                if current_node.nextNode is None:
                    current_node.nextNode = node
                    node.prevNode = current_node
                    return
                else:
                    current_node = current_node.nextNode

        else:
            while current_node:
                if index == pos:
                    node.nextNode = current_node
                    current_node.prevNode.nextNode = node
                    node.prevNode = current_node.prevNode
                    current_node.prevNode = node
                    return
                else:
                    current_node = current_node.nextNode
                    index += 1


    def remove(self, item):
        current_node = self.head
        if current_node is None:
            print('List is Empty')
        else:
            while current_node:
                if current_node.data == item:
                    current_node.prevNode.nextNode = current_node.nextNode
                    current_node.nextNode.prevNode = current_node.prevNode
                    del current_node
                    return 
                else:
                    current_node = current_node.nextNode


    # printList function print the list        
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.nextNode
        print('')


if __name__ == '__main__':
    n = DoublyLinkedList()
    n.insert_at_font(7)
    n.insert(9)
    n.insert_at_font(13)
    n.insert(3, 2)
    n.insert(21)
    n.insert(11, 2)
    n.remove(11)
    n.printList()

