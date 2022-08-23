class Queue():
    
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def __str__(self):
        return str(self.items)
    
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
x,y = input("Enter people and time : ").split()
mainQ, cQ1, cQ2 = Queue(),Queue(),Queue()
for i in range(len(x)):
    mainQ.enQueue(x[i])
for i in range(1,int(y)+1):
    if i%3 == 1 and i != 1:
        if cQ1.isEmpty() == False:
            cQ1.deQueue()
        else: pass
    if i%2 == 0:
        if cQ2.isEmpty() == False:
            cQ2.deQueue()
        else: pass
    if mainQ.isEmpty() == False:
        if cQ1.size() < 5:
            cQ1.enQueue(mainQ.deQueue())
        else:
            if cQ2.size() < 5:
                cQ2.enQueue(mainQ.deQueue())
            else:
                pass
    
    print(i,mainQ,cQ1,cQ2)

