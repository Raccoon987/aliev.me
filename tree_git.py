
''' create binary heap - list realization - acts like tree '''

class BinaryHeap:
    def __init__(self, size):
        self.heapList = [0]
        self.currentSize = 0
        self.maxSize = size    #max number of elements in heap

    # inserting element with it futher migration to the correct "binary heap" place
    def elementUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def insert(self, elem):
        # before insertion of the new element - look at the heap size - if it is too big than delete root
        if self.currentSize >= self.maxSize:
            self.delRoot()

        self.heapList.append(elem)
        self.currentSize += 1
        self.elementUp(self.currentSize)

    # deleting root element, by means of replacing with the last element of the list.
    # and futher migration to the correct "binary heap" place
    def findMinChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def elementDown(self, i):
        while i*2 <= self.currentSize:
            position = self.findMinChild(i)
            if self.heapList[i] > self.heapList[position]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[position]
                self.heapList[position] = temp
            i = position

    def delRoot(self):
        rootval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.elementDown(1)
        return rootval

    # creating binary heap from arbitrary list
    def buildHeap(self, lst):
        self.currentSize += len(lst)
        self.heapList += lst[:]

        i = self.currentSize // 2
        while (i > 0):
            self.elementDown(i)
            i = i - 1
        # keep heap less than self.maxSize
        for i in range(self.currentSize - self.maxSize):
            self.delRoot()

    # sort method using heap
    def heapSort(self, lst):
        self.buildHeap(lst)
        return [self.delRoot() for i in range(self.currentSize)]





''' class that makes max binary heap - max element at the root place '''
class MaxBinHeap(BinaryHeap):

    def __init__(self, size):
        BinaryHeap.__init__(self, size)

    #inserting element with it futher migration to the correct "binary heap" place
    #revrite method to put max element closer to the root
    def elementUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def elementDown(self, i):
        while i*2 <= self.currentSize:
            position = self.findMaxChild(i)
            if self.heapList[i] < self.heapList[position]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[position]
                self.heapList[position] = temp
            i = position

    def findMaxChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i*2 + 1
            else:
                return i*2




''' Queue with priority - realize it on the base of MaxBinHeap. new element put at the end
    of the list. if its number is big - it moves to the bigining of the list. begining of the list -
    place where the root element(the bigest number) stays - place where we make dequeue operation. '''

class PriorityQueue(MaxBinHeap):

    def __init__(self, size):
        MaxBinHeap.__init__(self, size)

    def enqueue(self, element):
        self.insert(element)

    def dequeue(self):
        self.delRoot()

    def isEmpty(self):
        return self.currentSize == 0

    def size(self):
        return self.currentSize





class TreeNode:

    def __init__(self, key, val, leftCh=None, rightCh=None, parent=None):
        self.key = key
        self.value = val
        self.leftChild = leftCh
        self.rightChild = rightCh
        self.parent = parent
        self.balanceFactor = 0

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for i in self.leftChild:
                    yield i
            yield self.key

            if self.hasRightChild():
                for j in self.rightChild:
                    yield j

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return (not self.rightChild) and (not self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, val, leftCh=None, rightCh=None):
        self.key = key
        self.value = val
        self.leftChild = leftCh
        self.rightChild = rightCh
        if self.hasRightChild():
            self.rightChild.parent = self
        if self.hasLeftChild():
            self.leftChild.parent = self

    def findSuccessor(self):
        # helper method to find successor of deleted node that has both left and right child
        successor = None
        # if remove node has right child, than successor - min key in the right subtree
        if self.hasRightChild():
            successor = self.rightChild.findMin()
        else:
            if self.parent:
                # if node has no right child but node is a left child of his parent, that this
                # parent will be successor
                if self.isLeftChild():
                    successor = self.parent
                # if node has no right child but node is a right child of his parent, than
                # successor will be his parent successor (excepting current node)

                # else:
                #    self.parent.rightChild = None
                #    successor = self.parent.findSuccessor()
                #    self.parent.rightChild = self

                elif self.isRightChild():
                    self.parent.rightChild = None
                    successor = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return successor

        # min key will be the most left of all seccessors

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent




''' Binary Tree Search
    Left child always less than root, right child > than root '''

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __setitem__(self, key, val):
        self.put(key, val)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    # walking the tree
    def walking_tree(self, node):
        if node:
            print(node.key, node.value)
            self.walking_tree(node.leftChild)
            # print (node.key, node.value)
            self.walking_tree(node.rightChild)
            # print (node.key, node.value)

    # put element to the binary search tree
    def put(self, key, val):
        # try to find element in the tree that already has suck key
        check = self._get(key, self.root)
        # if yes - change its value
        if check:
            check.value = val
        else:
            if self.root:
                self._put(key, val, self.root)
            else:
                self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, currNode):
        if key < currNode.key:
            if currNode.hasLeftChild():
                self._put(key, val, currNode.leftChild)
            else:
                currNode.leftChild = TreeNode(key, val, parent=currNode)
        else:
            if currNode.hasRightChild():
                self._put(key, val, currNode.rightChild)
            else:
                currNode.rightChild = TreeNode(key, val, parent=currNode)

    # get element from the tree
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, currNode):
        if not currNode:
            return None
        elif currNode.key == key:
            return currNode
        elif key < currNode.key and currNode.hasLeftChild():
            return self._get(key, currNode.leftChild)
        elif key > currNode.key and currNode.hasRightChild():
            return self._get(key, currNode.rightChild)

    # delete element from the tree
    def delete(self, key):
        if self.size > 1:
            # find element
            removeNode = self._get(key, self.root)
            if removeNode:
                self.remove(removeNode)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, removeNode):
        # Node has no children

        if removeNode.isLeaf():

            if removeNode.isLeftChild():
                removeNode.parent.leftChild = None
            else:
                removeNode.parent.rightChild = None

                # node has 2 children
        elif removeNode.hasBothChildren():

            successor = removeNode.findSuccessor()
            removeNode.key = successor.key
            removeNode.value = successor.value
            # deleting successor at his old place
            successor.spliceOut()

        # node has 1 children
        elif removeNode.hasAnyChildren():
            if removeNode.hasLeftChild():
                if removeNode.isLeftChild():
                    removeNode.parent.leftChild = removeNode.leftChild
                    removeNode.leftChild.parent = removeNode.parent
                elif removeNode.isRightChild():
                    removeNode.parent.rightChild = removeNode.leftChild
                    removeNode.leftChild.parent = removeNode.parent
                else:
                    # remove node is root
                    removeNode.replaceNodeData(removeNode.leftChild.key, \
                                               removeNode.leftChild.value, \
                                               removeNode.leftChild.leftChild, \
                                               removeNode.leftChild.rightChild)
            else:
                # remove node has right child
                if removeNode.isLeftChild():
                    removeNode.parent.leftChild = removeNode.rightChild
                    removeNode.rightChild.parent = removeNode.parent
                    # removeNode.parent.leftChild = removeNode.rightChild
                elif removeNode.isRightChild():
                    removeNode.parent.rightChild = removeNode.rightChild
                    removeNode.rightChild.parent = removeNode.parent
                    # removeNode.parent.rightChild = removeNode.rightChild
                else:
                    # remove node is root
                    removeNode.replaceNodeData(removeNode.rightChild.key, \
                                               removeNode.rightChild.value, \
                                               leftCh=removeNode.rightChild.leftChild, \
                                               rightCh=removeNode.rightChild.rightChild)



''' REALIZATION OF BALANCED TREE. height(letft subtree) - height(right subtree) = 0, +-1.
    subclass of BinarySearchTree '''

class BalancedSearchTree(BinarySearchTree):
    def __init__(self):
        # super(BalancedSearchTree, self).__init__()
        BinarySearchTree.__init__(self)

    # overloading _put() method
    def _put(self, key, val, currNode):
        if key < currNode.key:
            if currNode.hasLeftChild():
                self._put(key, val, currNode.leftChild)
            else:
                currNode.leftChild = TreeNode(key, val, parent=currNode)
                # use updateBalance method to maintain balance in tree
                self.updateBalance(currNode.leftChild)
        else:
            if currNode.hasRightChild():
                self._put(key, val, currNode.rightChild)
            else:
                currNode.rightChild = TreeNode(key, val, parent=currNode)
                # use updateBalance method to maintain balance in tree
                self.updateBalance(currNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            # return
        # updating balance factor of the new node parent
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

                # if balance factor of subtree = 0 than balance factor of it's tree does not change
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self, root):
        newRoot = root.rightChild
        root.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = root
        newRoot.parent = root.parent
        if root.isRoot():
            self.root = newRoot
        else:
            if root.isLeftChild():
                root.parent.leftChild = newRoot
            else:
                root.parent.rightChild = newRoot
        newRoot.leftChild = root
        root.parent = newRoot
        root.balanceFactor = root.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(root.balanceFactor, 0)

    def rotateRight(self, root):
        newRoot = root.leftChild
        root.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = root
        newRoot.parent = root.parent
        if root.isRoot():
            self.root = newRoot
        else:
            if root.isLeftChild():
                root.parent.leftChild = newRoot
            else:
                root.parent.rightChild = newRoot
        newRoot.rightChild = root
        root.parent = newRoot
        root.balanceFactor = root.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(root.balanceFactor, 0)




# nonrecursive tree traversal using findSuccessor method
# BUT NOT SYMMETRIC!!!
def fun(tree):
    i = 0
    start = tree.root.findMin()
    print
    start.key, start.value
    while i < tree.size - 1:
        i += 1
        start = start.findSuccessor()
        print
        start.key, start.value





if __name__ == "__main__":

    ''' testing BinaryHeap class '''
    binheap = BinaryHeap(20)
    for element in [14, 9, 5, 19, 11, 18, 21, 27, 7, 30, 1, 6, 25, 12, 18, 100]:
        binheap.insert(element)
    print(binheap.heapList)

    binheap.buildHeap([8,20,6,2,3])
    print("binary heap size: ", binheap.currentSize)
    print("binary heap list: ", binheap.heapList)

    for i in range(2):
        print("new root: ", binheap.delRoot())
        print("binary heap size: ", binheap.currentSize)
        print("binary heap list: ", binheap.heapList)

    binheap = BinaryHeap(10)
    binheap.buildHeap([2,5,4,7,6,22,21,15,14])
    print("testing buildHeap() method: ", binheap.heapList)
    print("sorted list: ", binheap.heapSort([17, 14, 9, 5, 19, 11, 18, 21, 27, 7, 30, 1, 6, 25, 12, 18, 100]))




    ''' testing BinaryHeap class '''
    maxbinheap = MaxBinHeap(20)
    for element in [14, 9, 5, 19, 11, 18, 21, 27, 7, 30, 1, 6, 25, 12, 18, 100]:
        maxbinheap.insert(element)
    print(maxbinheap.heapList)
    print("testing buildHeap() method: ", maxbinheap.buildHeap([17, 14, 9, 5, 19, 11, 18, 21, 27, 7, 30, 1, 6, 25, 12, 18, 100]))





    ''' testing Priority queue class '''
    priqueheap = PriorityQueue(10)
    for element in [14, 9, 5, 19, 11, 18, 21, 27, 7, 30]:
        priqueheap.insert(element)
    print(priqueheap.heapList)
    for element in [1, 6, 25, 12, 18, 100]:
        priqueheap.insert(element)
    print(priqueheap.heapList)
    priqueheap.dequeue()
    print(priqueheap.heapList)





    ''' testing binary search tree '''
    def binschtr_test(searchtree_type):
        mytree = searchtree_type
        mytree[3] = "walrus"
        mytree[4] = "racoon"
        mytree[6] = "lizard"
        mytree[2] = "beaver"
        mytree[5] = "cat"
        mytree[1] = "hamster"
        mytree[10] = "duck"

        # print(mytree.root.key)
        # print(mytree.root.hasLeftChild())
        # print(mytree.root.rightChild.value)

        print("------------")
        mytree.walking_tree(mytree.root)
        # for i in mytree.root:
        #    print(i, mytree[i])

        mytree.__delitem__(6)
        print("------------")
        mytree.walking_tree(mytree.root)
        # for i in mytree.root:
        #    print i, mytree[i]
        print("------------")
        # print(mytree.root.rightChild.rightChild.value)

    binschtr_test(BinarySearchTree())



    ''' testing balanced search tree '''
    mytree = BalancedSearchTree()
    mytree[1] = 'walrus'
    mytree[2] = 'beaver'
    mytree[3] = 'rat'
    mytree[4] = 'racoon'
    mytree[5] = 'lizard'
    mytree[6] = 'cat'
    mytree[7] = 'duck'

    mytree.walking_tree(mytree.root)
    print(mytree.root.leftChild.leftChild.value)
    mytree[6] = "owl"
    mytree.walking_tree(mytree.root)

    fun(mytree)