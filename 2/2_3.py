def odd_even(arr, s):
    result = []
    if(s == 'Odd'): t = 0
    elif(s == 'Even'): t = 1
    for i in range(t, len(arr), 2):
        result.append(arr[i])
    return result

print("*** Odd Even ***")
print('Enter Input : ', end='')
x, y, z = str(input()).split(',')
if(x == 'S'):
    result = odd_even(y, z)
    for i in result:
        print(i, end='')

elif(x == 'L'):
    y = list(y.split(' '))
    result = odd_even(list(y), z)
    print(result)