class DynamicArray:
    def __init__(self, capacity: int):
        self.array = [None] * capacity
    
    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        #print("set start")
        #print(self.array)
        
        self.array[i] = n

        #print(self.array)
        #print("set end")


    def pushback(self, n: int) -> None:
        #print("pushback start")
        #print(self.array)
        
        #print(self.getSize(), self.getCapacity())
        if self.getSize() == self.getCapacity():
            self.resize()
        
        self.array[self.getSize()] = n

        #print(self.array)
        #print("pushback end")

    def popback(self) -> int:
        #print("popback start")
        #print(self.array)
        
        element = self.array[self.getSize() - 1]
        self.array[self.getSize() - 1] = None

        #print(self.array)
        #print("popback end")

        return element
 

    def resize(self) -> None:
        #print("resize start")
        #print(self.array)
    
        for i in range(self.getCapacity()):
            self.array.append(None)

        #print(self.array)
        #print("resize end")

    def getSize(self) -> int:
        #print("getSize")

        #print(self.array)
        realItems = [item for item in self.array if item is not None]
        #print(len(s))

        return len(realItems)
        
    
    def getCapacity(self) -> int:
        #print("getCapacity")
        #print(len(self.array))

        return len(self.array)

