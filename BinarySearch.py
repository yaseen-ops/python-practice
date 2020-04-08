pos = 'dummy'
def search(list, n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid+1
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u=mid+1
    return False

list = [3,5,7,9,1]
n = 9

if search(list, n):
    print('Found at', pos)
else:
    print('Not Found')