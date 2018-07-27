# unordered linked list
class Node:
    def __init__(self, initdata, position=0):
        self.data = initdata
        self.next = None
        self.position = position

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPosition(self):
        return self.position

    def setPosition(self, pos):
        self.position = pos

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def __str__(self):
        return str(self.data)


class OrderedList:
    def __init__(self):
        self.head = None

    def index(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return current.getPosition()
            else:
                current = current.getNext()
        print("item not present in list")

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

        self.index_correct(self.head)

    # helper function
    def index_correct(self, value):
        position = 0
        while value != None:
            value.setPosition(position)
            position += 1
            value = value.getNext()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self, item):
        if self.head == None:
            # raise IndexError("pop from empty list")
            print("No such element in the list")
            return None

        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found == True and previous == None and current.getNext() == None:
            # one element in list
            self.head = None
        elif found and previous == None:
            self.head = current.getNext()
        elif found == True and current.getNext() == None:
            # the last element
            previous.setNext(None)
        elif found == True:
            previous.setNext(current.getNext())
        else:
            print("No such element in the list")

        self.index_correct(self.head)

    def pop(self):
        if self.head == None:
            print("There is no elements for poping in the list")
            return None
        current = self.head
        previous = None
        if self.size() == 1:
            self.head = None
            return None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        previous.setNext(None)
        return current

    def __str__(self):
        data = []
        curr = self.head
        while curr is not None:
            data.append(curr.getData())
            curr = curr.getNext()
        return "[%s]" % (', '.join(str(i) for i in data))

    def __repr__(self):
        return self.__str__()


mylist = OrderedList()


def info():
    print(mylist, mylist.head)
    print("\n")

def lst_filling(lst):
    for i in lst:
        mylist.add(i)
    info()

def ind(lst):
    print([mylist.index(i) for i in lst])

def poping():
    mylist.pop()
    info()


lst_filling([7, 77, 1, 0, 25, -5])
ind([77, 0, 25, -5])
[(mylist.remove(i), info()) for i in [10, -5, 7, 77, 1, 0, 25]]

lst_filling([7, 77, 1, 0, 25, -5])
[mylist.remove(i) for i in [-5, 77, 0, 25]]
info()
ind([7, 0, 25, 1])

poping()
poping()
poping()