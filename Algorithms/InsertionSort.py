l = [-1, 4, 4, 5, -2, 0, 7, -3, 8]

#l = [12, 11, 13, 5, 6, 7]

def insertionSort (arr):
    for i in range (1, len(arr)):
        aux = arr[i]
        j = i-1
        while j >= 0 and arr[j] > aux:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = aux

insertionSort(l)
#print(l)

def f(l):
    print("A")
    if l == []:
        raise ValueError()
    print("B")

def start():
     l = []
     try:
        print("A")
        f(l)
        print("D")
     except ValueError:
        print("C")
#start()
class A:
 def f(self, l,nr):
  l.append(nr)
class B:
 def g(self, l, nr):
  nr=nr-1
  l = l+[-2]
  #print(l)
a = A()
b = B()
l = [1,2]
c = -1
a.f(l,6)
b.g(l,c)
#print(l,c)


a = lambda x: [x+1]
b = a(1)
c = lambda x: x + b
d = c([1])
a = 1
b = 3
#print (a, b, c(4), d[1])


l = [1,2,3,4,5]
l2 = {}
l = [1]

def sum_even(l):
    if type(l) != list:
        raise TypeError
    s = 0
    ok = 0
    for i in l:
        if i%2 == 0:
            ok = 1
            s += i
    if ok == 0:
        raise ValueError
    return s

#print(sum_even(l))


def function(n):
     '''
     Checks wether or not a number is prime
     Input:
        - n - natural  number different from 0 1
     Output:
        True : if n is prime False otherwise
     '''
     d = 2
     while (d < n - 1) and n % d > 0:
        d += 1
     return d >= n - 1

def test_function():
    l = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    for i in range(2,50):
        #print(i, function(i), i in l)

        if i in l:
            assert function(i) == True
        else:
            assert function(i) == False
def complexity_2(x):
     found = False
     print(x)
     n = len(x) - 1
     while n != 0 and not found:
        print(x[n])
        if x[n] == 7:
            found = True
        else:
            n = n - 1
     return found

print(complexity_2([7,2,3]))