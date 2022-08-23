x = int(input("Enter Input : "))
for i in range(0,6+2*(x-1),1):
    for j in range(i,x+1,1):
        print(".",end='')
    for j in range(0,i+1,1):
        if(j>=x+2) : break
        if(i>=x+3 and i < x+x+3) : 
            print("#",end='')
            for k in range(x):
                print("+",end='')
            print("#",end='')
            break
        print("#",end='')
    for j in range(x+3,i+1,-1):
        if(i==x+1):break
        print("+",end='')
        if(i>=1 and i<=x) :
            for k in range(x):
                print("#",end='');
            print("+",end='')
            break
    if(i==x+1):
        for j in range(0,x+2,1):
            print("+",end='')
    elif (i > x+1):
        for j in range(6+2*(x-1),i,-1):
            print("+",end='')
        for j in range(x+2,i,1):
            print(".",end='')
    print()
            