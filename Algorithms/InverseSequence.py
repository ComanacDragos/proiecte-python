#l = [-1, 4, 4, 5, -2, 0, 7, -3, 8]

l = [12, 11, 13, 5, 6, 7]

"""def DEI (arr, l, r):
    if l == r:
        return [arr[l]] # cazul de baza
    m = (l+r)//2 # pivotul !! nu este necesar sa fie media aritmetica dintre l si r
    return DEI(arr, m+1, r) + DEI(arr, l, m)
"""


def DEI (arr, l, r):
    if l == r:
        return [arr[l]] # cazul de baza
    m = l # pivotul !! nu este necesar sa fie media aritmetica dintre l si r
    return DEI(arr, m+1, r) + DEI(arr, l, m)
print(DEI(l,0 ,len(l)-1))

def hanoi(n, x, y, z):
    '''
    n - number of disks on the x stick
    x - source Stick
    y - destination stick
    z - intermediate stick
    '''
    if n == 1:
        return
    hanoi(n - 1, x, z, y)
    hanoi(n - 1, z, y, x)



def hanoiVerbose(n, x, y, z):
    '''
    n - number of disks on the x stick
    x - source Stick
    y - destination stick
    z - intermediate stick
    '''
    if n == 1:
        print("Disk 1 from " , x , " to " , y)
        return
    hanoiVerbose(n - 1, x, z, y)
    print("Disk ", n, " from ", x, " to ", y)
    hanoiVerbose(n - 1, z, y, x)


#hanoiVerbose(3,1,2,3)


a = 1
b = 2


print(a,b)
a,b = b,a
print(a,b)

for i in filter(lambda x : x%2==1, l):
    print(i)

g = lambda x : x+3+4+5

#print(g(3))