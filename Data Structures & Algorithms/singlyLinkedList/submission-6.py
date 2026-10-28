class Node:
    def __init__(self, head, tail, value):
        self.head = head
        self.tail = tail
        self.value = value
    
    def setHead(self, head):
        self.head = head
    
    def setTail(self, tail):
        self.tail = tail
    
    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail
    
    def getValue(self):
        return self.value

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        n = self.head
        if n == None:
            return -1
        
        for i in range(index):
            if n.getTail() == None:
                return -1
            n = n.getTail()

        return n.getValue()
        

    def insertHead(self, val: int) -> None:
        if self.head == None:
            n = Node(None, None, val)
            self.head = n
            self.tail = n
        else:
            n = Node(None, self.head, val)
            self.head.setHead(n)
            self.head = n

    def insertTail(self, val: int) -> None:
        if self.tail == None:
            n = Node(None, None, val)
            self.head = n
            self.tail = n
        else:
            n = Node(self.tail, None, val)
            self.tail.setTail(n)
            self.tail = n

    def remove(self, index: int) -> bool:
        n = self.head
        if n == None:
            return False

        for i in range(index):
            n = n.getTail()
            if n == None:
                return False
        
        if n.getHead() != None:
            n.getHead().setTail(n.getTail())
        else:
            self.head = n.getTail()

        if n.getTail() != None:
            n.getTail().setHead(n.getHead())
        else:
            self.tail = n.getHead()


        return True


    def getValues(self) -> List[int]:
        values = []

        n = self.head
        while n != None:
            values.append(n.getValue())
            n = n.getTail()
        
        return values
        