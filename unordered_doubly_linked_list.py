#double linked list

class Node:
    def __init__(self, initdata, position = 0):
        self.data = initdata
        self.next = None
        self.previous = None
        self.position = position 
        
        
    def getData(self):
        return self.data

    def setData(self,newdata):
        self.data = newdata

    def getNext(self):
        return self.next
    
    def setNext(self,newnext):
        self.next = newnext
        
    def getPrev(self):
        return self.previous
    
    def setPrev(self,newprevious):
        self.previous = newprevious    
        
    def __str__(self):
        return str(self.data)
    
    def setPos(self, position):
        self.position = position
        
    def getPos(self):
        return self.position    
    
           
class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def index(self,item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return current.getPos()
            else:
                current = current.getNext()
        print ("item not present in list")
    
    
    #helper function for correcting index after poping, adding and so all
    def index_correct(self, value):
        position = 0
        while value != None:
            value.setPos(position)
            position += 1
            value = value.getNext()
    
    
    def isEmpty(self):
        return self.head == None
    
    
    #add to the list begining (to the head) i.e. to the left side 
    def add(self,item):
        temp = Node(item)
        if self.head is None:
            self.tail = temp
            temp.setPrev(None)   
            temp.setNext(self.head) 
        else:
            temp.setNext(self.head)
            self.head.setPrev(temp)
              
        self.head = temp
        #correcting index
        self.index_correct(self.head)
        
    
    #add to the end of the list (to the tail) i.e. to the right side 
    def append(self, item):      
        temp = Node(item)
        if self.head is None:
            self.tail = temp
            temp.setPrev(self.head)
            temp.setNext(None) 
            #temp.setNext(self.head) 
            self.head = temp
        else:
            self.tail.setNext(temp)
            temp.setPrev(self.tail)    
            temp.setNext(None)
            self.tail = temp
        self.index_correct(self.head)
        
    
    #insert to the exact position
    def insert(self, item, position):
        if self.isEmpty() and position == 0:
            self.add(item) 
        elif position == 0:
            self.add(item)
        elif position > self.size():
            print("position index out of range")
        elif position == self.size() or position == -1:
            self.append(item)
        else:
            
            temp = Node(item)
            current = self.head
            #while (current is not None) and (current.getPos() != position):
            while current.getPos() != position:
                current = current.getNext()   
            (current.getPrev()).setNext(temp)
            temp.setPrev(current.getPrev())
            temp.setNext(current)
            current.setPrev(temp) 
            
            self.index_correct(self.head)            
        
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count  
    
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
    
        if found:
            return current
        else:
            return found   
    
    
    def remove(self,item):
                
        if self.isEmpty():
            print("You can not remove nothing from the empty list")
            return None
        
        current = self.head
        found = False
                    
        while not found and current != None:
            if current.getData() == item:
                found = True 
            else:
                current = current.getNext()     
    
        if found == True and current.getPrev() == None and current.getNext() == None:
            #one element in list
            self.head = self.tail = None
        elif found == True and current.getPrev() == None:
            #first element
            self.head = current.getNext()
            self.head.setPrev(None)
        elif found == True and current.getNext() == None:
            #the last element
            self.tail = current.getPrev()
            (current.getPrev()).setNext(None) 
            #current.setPrev(None)
        elif found == True:
            (current.getPrev()).setNext(current.getNext())
            (current.getNext()).setPrev(current.getPrev())
        else:
            print("No such element in the list")
        
        self.index_correct(self.head)
        
              
    def pop(self):
        #if self.head == None:
        #    raise IndexError("pop from empty list")

        if self.size() > 1:
            poped_el = self.tail
            self.tail.getPrev().setNext(None)
            self.tail = self.tail.getPrev()
            self.index_correct(self.head)
        elif self.size() == 1:
            poped_el = self.tail
            self.tail = self.head = None
            self.index_correct(self.head)   
        else:
            print("the list is empty")
            return None     
        return poped_el
                               
    #DO NOT SLICE THE WHOLE LIST !!!!!    
    def slice(self, start, stop):
        if start > stop or start < 0 or stop > self.size():
            print("Bad slice")
            return None
        sliced_lst = UnorderedList()
        curr = self.head
        
        #flag for situation when the stop position = last element
        #without this 'NoneType' object has no attribute 'getPos' occures
        flag = False
        if stop == self.size():
            stop = stop - 1
            flag = True
             
        while curr.getPos() < stop:
            if curr.getPos() >= start:
                sliced_lst.append(curr.getData())
            curr = curr.getNext()
        
        if flag:
            sliced_lst.append(curr)
        return sliced_lst
            
    
    #get Node
    #returns Node instance by it position
    def get_node(self, index):
        if 0 <= index < self.size():
            current = self.head
            #while (current is not None) and (current.getPos() != index):
            while current.getPos() != index:
                current = current.getNext()
            return current
                
    
    def __str__(self):
        data = []
        curr = self.head
        while curr is not None:
            data.append(curr.getData())
            curr = curr.getNext()
        return "[%s]" %(', '.join(str(i) for i in data))
        
        
    
    def __repr__(self):
        return self.__str__()                               
 

    def clear(self):
        self.__init__()






#CREATING Stack, 
class Stack(UnorderedList):
     def __init__(self):
         UnorderedList.__init__(self)

     def stack_isEmpty(self):
         return self.isEmpty()

     def push(self, item):
         self.append(item)

     def stack_pop(self):
         return self.pop()

     def peek(self):
         #return self.items[len(self.items)-1]
         return self.slice(self.size() - 1, self.size())

     def stack_size(self):
         return self.size()



class Queue(UnorderedList):
    def __init__(self):
        UnorderedList.__init__(self)

    def queue_isEmpty(self):
        return self.isEmpty()

    def enqueue(self, item):
        self.add(item)

    def dequeue(self):
        return self.pop()

    def queue_size(self):
        return self.size()



class Deque(UnorderedList):
    def __init__(self):
        UnorderedList.__init__(self)

    def deque_isEmpty(self):
        return self.isEmpty()

    def addFront(self, item):
        self.append(item)

    def addRear(self, item):
        self.add(item)

    def removeFront(self):
        return self.pop()

    def removeRear(self):
        #print(self.slice(0, 1).get_node(0).__class__)
        return self.remove((self.slice(0, 1).get_node(0)).getData())

    def deque_size(self):
        return self.size()






''' functions to check correctness  '''
def info(mylist):
    print("list: ", mylist, " head: ", mylist.head, " tail: ", mylist.tail)

def lst_filling(mylist, add_num=[31, 77, 17], append_num=[93, 26, 54]):
    for i in add_num:
        mylist.add(i)
        info(mylist)
    for i in append_num:
        mylist.append(i)
        info(mylist)




if __name__ == "__main__":
    # b = UnorderedList()
    # b.append(1)
    # b.append(2)
    # print b.get_node(0).getData()

    '''
    a = Deque()
    print(a.deque_isEmpty())
    for i in range(1, 7):
        a.addFront(i)
    print(a.deque_size())
    for i in range(6):
        a.removeRear()
        print(a.deque_size())
    '''

    mylist = UnorderedList()

    lst_filling(mylist)
    print("slice from 1 to 4 element: ", mylist.slice(1, 4))
    print("\n")

    print("insertion ")
    for i in [100, 101, 102]:
        mylist.insert(i, -1)
        info(mylist)
    print("\n")

    print("indexing")
    for i in [17, 77, 31, 93, 26, 54]:
        print(i, " index: ", mylist.index(i), end="; ")
    print("\n")

    print("removing first elements")
    for i in [17, 77, 31, 93, 26, 54, 1000]:
        print("remove element: ", i)
        mylist.remove(i)
        info(mylist)
    print("\n")

    print("filling")
    lst_filling(mylist)
    info(mylist)
    print("\n")

    print("removing last elements")
    for i in [54, 26, 93, 1000]:
        print("remove element: ", i)
        mylist.remove(i)
        info(mylist)
    print("\n")

    lst_sz = mylist.size()
    print("list size: ", lst_sz)
    print("\n")

    print("poping")
    for i in range(0, lst_sz):
        print("pop element: ", mylist.pop())
        info(mylist)
    print("\n")

    print("list is empty: ", mylist.isEmpty())