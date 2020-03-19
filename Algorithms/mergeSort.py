l = [-1, 4, 4, 5, -2, 0, 7, -3, 8,]


'''
1 2  3 4 5
4 5 -2 0 7

pivot = 4
l=1
r=5

-> 
l = 1
j = 4
0 5 -2 0 7

->
l = 2
j = 4
0 5 -2 5 7
 
->
0 4 -2 5 7

'''


#l = [12, 11, 13, 5, 6, 7]

def merge (l1, l2):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            l.append(l2[j])
            j += 1
        else:
            l.append(l1[i])
            i += 1

    while i < len(l1):
        l.append(l1[i])
        i += 1

    while j < len(l2):
        l.append(l2[j])
        j += 1

    return l

def merge_sort (l):
    if len(l) == 1:
        return l

    m = len(l)//2
    l1 = l[:m]
    l2 = l[m:]
    return merge(merge_sort(l1), merge_sort(l2))

#print(merge_sort(l))

l = [-1, 4, 4, 5, -2, 0, 7, -3, 8,]
#l = [12, 11, 13, 5, 6, 7]

def partition (arr, l, r):
    pivot = arr[l]
    i = l
    j = r

    while i != j:
        while arr[j] >= pivot and i<j:
            j -= 1
        arr[i] = arr[j]

        while arr[i] <= pivot and i<j:
            i += 1
        arr[j] = arr[i]
    arr[i] = pivot
    return i

def quickSort (arr, l, r):
    pos = partition(arr, l, r)
    if pos+1 < r:
        quickSort(arr, pos+1,r)
    if pos-1 >l:
        quickSort(arr, l,pos-1)

quickSort(l, 0, len(l)-1)
print(l)

from sys import maxsize

size = maxsize
print(size)