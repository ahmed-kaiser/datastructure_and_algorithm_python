# --- Implementation of BST ---
class BinarySearchTree:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # adds node to the tree
    def insert(self, item):
        if self.data == item:
            # item already exist
            return

        elif self.data is None:
            # root is none
            self.data = item

        elif self.data > item:
            # goes left of the tree 
            if self.leftChild is None:
                self.leftChild = BinarySearchTree(item)
            else:
                self.leftChild.insert(item)

        elif self.data < item:
            # goes right of the tree 
            if self.rightChild is None:
                self.rightChild = BinarySearchTree(item)
            else:
                self.rightChild.insert(item)


    # search a specific item in the tree if found return true else false
    def search(self, item):
        if item == self.data:
            return True

        if item < self.data:
            # searchs left of the tree
            if self.leftChild:
                return self.leftChild.search(item)
            else:
                return False

        elif item > self.data:
            # searchs right of the tree
            if self.rightChild:
                return self.rightChild.search(item)
            else:
                return False


    def findMax(self):
        if self.rightChild:
            return self.rightChild.findMax()
        else:
            return self.data


    def findMin(self):
        if self.leftChild:
            return self.leftChild.findMin()
        else:
            return self.data


    def findHeight(self, node):
        if node is None: 
            return 0

        else:
            leftHeight = self.findHeight(node.leftChild)
            rightHeight = self.findHeight(node.rightChild)

            return max(leftHeight, rightHeight) + 1


    def preorder(self):
        print(self.data, end=' ')
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.data, end=' ')


    def in_order(self):
        if self.leftChild:
            self.leftChild.in_order()
        print(self.data, end=' ')
        if self.rightChild:
            self.rightChild.in_order()


    def levelOreder(self, node):
        que = [] # works as queue manner
        que.append(node)

        while que:
            print(que[0].data, end=' ')
            
            if node.leftChild:
                que.append(node.leftChild)
            if node.rightChild:
                que.append(node.rightChild)

            que.pop(0)

            if que:
                node = que[0]


    def delete(self, item):
        if self.data > item:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(item)

        elif self.data < item:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(item)

        else:
            if self.leftChild is None and self.rightChild is None:
                # node have no child
                return None
            elif self.leftChild is None:
                # node have only right child
                return self.rightChild
            elif self.rightChild is None:
                # node have only left child
                return self.leftChild
            else:
                # node have both child
                min_max = self.leftChild.findMax()
                self.data = min_max
                self.leftChild = self.leftChild.delete(min_max)

        return self
            

            
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    bst.insert(7)
    bst.insert(19)
    bst.insert(3)
    bst.insert(11)
    bst.insert(21)
    bst.insert(20)
    bst.insert(8)

    # print(bst.search(10))
    # print(bst.get_root())
    # print(bst.findMax())
    # print(bst.findMin())
    # print(bst.findHeight(bst))
    bst.preorder()
    # print('')
    # bst.postorder()
    # print('')
    # bst.delete(15)
    # bst.in_order()
    # print('')
    # bst.levelOreder(bst)
