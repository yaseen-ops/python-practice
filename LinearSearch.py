#For Loop
pos = 'Dummy'
def search(list, n):
    for i in list:
        if i == n:
            globals() ['pos'] = list.index(n)+1   # +1 is added to make human readable, as list starts from '0'
            return True

list = [3,5,7,9,1]
n = 9

if search(list, n):
    print('Found at', pos)
else:
    print('Not Found')

#While Loop
pos = 'Dummy'
def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos']=i+1  # +1 is added to make human readable, as list starts from '0'
            return True
        i = i +1
    return False

list = [3,5,7,9,1]
n = 9

if search(list, n):
    print('Found at', pos)
else:
    print('Not Found')