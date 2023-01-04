class Node:
    def __init__(self, init_data):
        self.data=init_data
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data=newdata
    def setNext(self, new_next):
        self.next=new_next

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
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
        return found

    
    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
            
###
    def insertPrevious(self, item, newNode):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                if previous == None:
                    temp = Node(newNode)
                    temp.setNext(self.head)
                    self.head = temp

                else:
                    temp = Node(newNode)
                    temp.setNext(current)
                    previous.setNext(temp)
            else:
                previous = current
                current = current.getNext()
        
    def insertNext(self, item, newNode):
        current = self.head
        next_ = self.head.getNext()
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                next_ = next_.getNext()
                current = current.getNext()
        if next_ == None:
            temp = Node(newNode)
            temp.setNext(None)
            current.setNext(temp)

        else:
            temp = Node(newNode)
            temp.setNext(next_)
            current.setNext(temp)
###


mylist = LinkedList()
mylist.add(10)
mylist.add(20)
mylist.add(35)
mylist.add(40)
print("Data =")
mylist.display()
print('')
print("Insert Previous")
a = int(input("Data yang ingin dimasukkan = "))
b = int(input("sebelum data = "))
mylist.insertPrevious(b, a)
mylist.display()


