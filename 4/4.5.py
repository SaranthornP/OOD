class Stack():
    
    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = ls
            
    def __str__(self):
        return str(self.items)
    
    def push(self,i):
        self.items.append(i)
        
    def pop(self):
        self.items.pop()
    
    def pop2(self,i):
        self.items.pop(i)
        
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
    
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
    
n,m = input("Enter Input (Normal, Mirror) : ").split()

mirrorS = Stack()
mirrorQ = Queue()
normalS = Stack()
normalQ = Queue()
for i in range(len(m)):
    mirrorS.push(m[i])
i=mirrorS.size()-1
while i > -1:
    if i-2 > -1 and mirrorS.items[i] == mirrorS.items[i-1] and mirrorS.items[i-1] == mirrorS.items[i-2] :
        mirrorQ.enQueue(mirrorS.items[i])
        for j in range(3):
            mirrorS.pop2(i-2)
        i = mirrorS.size()
    else:
        pass
    i -= 1
explosiveMirrorBomb = mirrorQ.size()
normalExCount = 0
failedCount = 0
i=0

while i < len(n):
    if i+2 < len(n) and n[i] == n[i+1] and n[i+1] == n[i+2] :
        if mirrorQ.isEmpty() == False:
            for j in range(2):
                normalS.push(n[i])
            normalS.push(mirrorQ.deQueue())
            normalS.push(n[i+2])
            if normalS.size()-3 >= 0 and normalS.items[normalS.size()-1] == normalS.items[normalS.size()-2] and normalS.items[normalS.size()-2] == normalS.items[normalS.size()-3]:
                normalQ.enQueue(normalS.items[normalS.size()-1])
                for j in range(3):
                    normalS.pop()
                failedCount += 1
            else :
                pass
        else:
            normalExCount += 1
        
        i += 3
    else:
        normalS.push(n[i])
        i += 1
        
i = 0
while i < normalS.size():
    if i+2 < normalS.size() and normalS.items[i] == normalS.items[i+1] and normalS.items[i+1] == normalS.items[i+2]:
        normalExCount += 1
        for j in range(3):
            normalS.pop2(i)
        i = -1
    else:
        pass
    i += 1

print("NORMAL :")
print(normalS.size())
if normalS.size() != 0:
    print("".join(reversed(normalS.items)))
else:
    print("Empty")
print(normalExCount,"Explosive(s) ! ! ! (NORMAL)")
if failedCount != 0:
    print("Failed Interrupted {0} Bomb(s)".format(failedCount))
else:
    pass
print("------------MIRROR------------")
print(": RORRIM")
print(mirrorS.size())
if mirrorS.isEmpty() == False:
    BombInMirror = mirrorS.items
    print(("".join(BombInMirror)))
else:
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE",explosiveMirrorBomb)
    