print("*** Fun with Drawing ***")
x = int(input("Enter input : "))
for i in range((x-1)*2):
    if i%2==0 :
        for j in range((x-1)*4+1):
            if (j%2==1 and j <= i ) or (j%2==1 and (x-1)*4 - i <= j):
                print('.',end='')
            else :
                print('#',end='')
    else :
        for j in range((x-1)*4+1):
            if j == 0 or j == (x-1)*4 : 
                print('#',end='');
            elif (j%2==0 and j <= i ) or (j%2==0 and (x-1)*4 - i <= j) :
                print('#',end='')
            else :
                print('.',end='')
    print()
for i in range((x-1)*2):
    print("#.",end='')
print('#')
for i in range((x-1)*2-1,-1,-1):
    if i%2==0 :
        for j in range((x-1)*4,-1,-1):
            if (j%2==1 and j <= i ) or (j%2==1 and (x-1)*4 - i <= j):
                print('.',end='')
            else :
                print('#',end='')
    else :
        for j in range((x-1)*4,-1,-1):
            if j == 0 or j == (x-1)*4 : 
                print('#',end='');
            elif (j%2==0 and j <= i ) or (j%2==0 and (x-1)*4 - i <= j) :
                print('#',end='')
            else :
                print('.',end='')
    print()
    
