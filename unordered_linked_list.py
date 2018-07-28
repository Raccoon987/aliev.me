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

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def __str__(self):
        return str(self.data)

    def setPos(self, position):
        self.position = position

    def getPos(self):
        return self.position


class UnorderedList:
    def __init__(self):
        self.head = None

    def index(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return current.getPos()
            else:
                current = current.getNext()
        print("item not present in list")

    # helper function
    def index_correct(self, value):
        position = 0
        while value != None:
            value.setPos(position)
            position += 1
            value = value.getNext()

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

        # correcting index
        self.index_correct(self.head)

    # DOES NOT INSERT AT THE LAST POSITION!!!
    def insert(self, item, position):
        if self.isEmpty() and position == 0:
            self.add(item)
        elif position == 0:
            self.add(item)
        elif position > self.size():
            print("position index out of range")
        else:

            temp = Node(item)
            current = self.head
            previous = None

            #while (current.getPos() != position):
            while (current is not None) and (current.getPos() != position):
                previous = current
                current = current.getNext()
            previous.setNext(temp)
            temp.setNext(current)

            self.index_correct(self.head)

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
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        if self.isEmpty():
            print("You can not remove nothing from the empty list")
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
        elif found == True and previous == None:
            # the first element
            self.head = current.getNext()
        elif found == True and current.getNext() == None:
            # the last element
            previous.setNext(None)
        elif found == True:
            previous.setNext(current.getNext())
        else:
            print("No such element in the list")

        self.index_correct(self.head)

    def __str__(self):
        data = []
        curr = self.head
        while curr is not None:
            data.append(curr.getData())
            curr = curr.getNext()
        return "[%s]" % (', '.join(str(i) for i in data))

    def __repr__(self):
        return self.__str__()






# verification
def info():
    print(mylist, mylist.head)
    print("\n")


def lst_filling():
    for i in [31, 77, 17, 93, 26, 54]:
        mylist.add(i)
        info()


mylist = UnorderedList()


print("filling")
lst_filling()

print("indexing")
for i in [54, 26, 93, 17, 77, 31]:
    print(mylist.index(i))
print("\n")

print("removing first")
for i in [54, 26, 93, 17, 77, 31, 1000]:
    mylist.remove(i)
    info()

print("filling")
lst_filling()

print("removing last")
for i in [31, 77, 17, 93, 26, 54, 1000]:
    mylist.remove(i)
    info()

print("filling")
lst_filling()

print("removing from inside")
for i in [26, 31, 93, 17, 77, 54, 1000]:
    mylist.remove(i)
    info()

print(mylist.isEmpty())




print("filling")
lst_filling()
mylist.remove(777)

info()
for i in [100, 101, 102]:
    mylist.insert(i, 6)
    info()




'''
mylist = UnorderedList() 

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)  

print(mylist)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))  
'''