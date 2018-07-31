#"MAP" abstraction (smth. like dictionary) hash table with linear probing

class HashTable():

    TOMBSTONE = '<Tombstone>'
    resize_lst = [11, 23, 43, 67, 127, 173, 683]
    index = 0

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def utilization(self):
        #Calculate the number of buckets that are populated or tombstoned
        try:
            return float(len(self))/float(self.size)
        except ZeroDivisionError:
            return 0

    def _resize(self, new_size):
        #increase size of hashtable
        #This method recreates the list and reinserts all old records
        #at their computed hashes.    
        old_slots = self.slots
        old_data = self.data

        self.size = new_size
        self.slots = [None] * self.size
        self.data = [None] * self.size

        for i in old_slots:
            if i != None and i != self.TOMBSTONE:
                self.put(i, old_data[old_slots.index(i)])





    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return len([i for i in self.slots if i and i != self.TOMBSTONE]) 
        #return self.size        

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)    




    def put(self, key, value):
        if self.utilization() > 0.75:
            self._resize(self.resize_lst[self.index + 1])
            self.index += 1

        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None or self.slots[hashvalue] == self.TOMBSTONE:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:

            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value #rewrite
            else:
                nextslot = self.rehash(hashvalue, self.size)    
                while self.slots[nextslot] != None and self.slots[nextslot] != key and self.slots[nextslot] != self.TOMBSTONE:
                    nextslot = self.rehash(nextslot, self.size)   

                if self.slots[nextslot] == None or self.slots[nextslot] == self.TOMBSTONE:
                    self.slots[nextslot] = key
                    self.data[nextslot] = value
                else:
                    self.data[nextslot] = value

    def get(self, key):
        startslot = self.hashfunction(key, self.size)

        value = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key:
                found = True
                value = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == startslot:
                    stop = True     
        return value  


    def delete(self, key):
        startslot = self.hashfunction(key, self.size)

        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key:
                found = True
                self.slots[position] = self.TOMBSTONE
            else:
                position = self.rehash(position, self.size)
                if position == startslot:
                    stop = True     

        if 0 < self.utilization() <= 0.16 and self.index > 0:
            self._resize(self.resize_lst[self.index - 1])
            self.index -= 1




a = HashTable()
a[15] = "racoon"
a[24] = "walrus"
a[77] = "crow"
a[55] = "lizard"
a[43] = "pig"
a[83] = "fox"
a[51] = "peacock"

keys = [15, 24, 77, 55, 43, 83, 51, 18, 75] 
print([i%11 for i in keys])
print("---------------")
print("Hash Table")
print(a.slots)
print(a.data)
print("Amount of elements")
print(len(a))
print("15 is in hash table")               
print(15 in a)
print("60 is in hash table") 
print(60 in a)
print("Table filling")
print(a.utilization())      
#rename
print("rename elements 15 and 77")
a[15] = "RACOON"
a[77] = "CROW"
print(a.slots)
print(a.data)
print("---------------")
print("add more elements")
a[18] = "beaver"
print("Table filling")
print(a.utilization()) 
a[75] = "elephant" 
print("Table filling")
print(a.utilization()) 
print(a.slots)
print(a.data)
#deleting
print("---------------")
print("delete 15")
print(15 in a)
print("Amount of elements")
print(len(a))
print("15 is in hash table") 
del a[15]
print("Amount of elements")
print(len(a))
print("15 is in hash table")
print(15 in a)
print(a.slots)
print(a.data)
print("---------------")
print("add element at ex-15 position")
a[26] = "RaCoOn"
print(a.slots)
print(a.data)
print("---------------")
print("add one more element")
a[14] = "dragon"
keys = [26, 24, 77, 55, 43, 83, 51, 18, 75, 14] 
print([i%23 for i in keys])
print(a.slots)
print(a.data) 
print("---------------")
print("add 2 more elements with collision - 32 and 78")
print("they should appear after 'lizard'")
a[32] = "worm"
a[78] = "sheep"
print(a.slots)
print(a.data)
print("delete element 32")
del a[32]
print("try to find element 78")
print(a[78])
print("---------------")
print("delete more two elements - 78 and 14")
del a[78]
del a[14]
del a[55]
del a[83]
del a[26]
del a[75]
del a[18]
del a[51]
print(a.slots)
print(a.data)
print(a.utilization()) 