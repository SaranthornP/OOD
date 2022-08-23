class Queue():
    
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
x = list(input("Enter Input : ").split(','))

myQ = Queue()
yourQ = Queue()
mTranQ = Queue()
yTranQ = Queue()
score = 0
for i in range(len(x)):
    y = x[i].split(' ')
    myQ.enQueue(y[0])
    yourQ.enQueue(y[1])
    for j in range(2):
        m,m2 = y[j].split(':')
        my,you="",""
        location = ["Res." , "ClassR.", "SuperM.", "Home"]
        activity = ["Eat", "Game", "Learn", "Movie"]
        if j == 0:
            for k in range(4):
                if int(m) == k:
                    my += activity[k] + ":"
            for k in range(4):
                if int(m2) == k:
                    my += location[k]
            mTranQ.enQueue(my)
        else:
            for k in range(4):
                if int(m) == k:
                    you += activity[k] + ":"
            for k in range(4):
                if int(m2) == k:
                    you += location[k]
            yTranQ.enQueue(you)
    if y[0][0] == y[1][0] and y[0][2] == y[1][2]:
        score += 4
    elif y[0][0] == y[1][0]:
        score += 1
    elif y[0][2] == y[1][2]:
        score += 2
    else:
        score -= 5
        
print("My   Queue =",(', ').join(myQ.items))
print("Your Queue =",(', ').join(yourQ.items))
print("My   Activity:Location =",(', ').join(mTranQ.items))
print("Your Activity:Location =",(', ').join(yTranQ.items))
if score >= 7:
    print("Yes! You're my love! : Score is {0}.".format(score))
elif score < 7 and score > 0:
    print("Umm.. It's complicated relationship! : Score is {0}.".format(score))
else:
    print("No! We're just friends. : Score is {0}.".format(score))