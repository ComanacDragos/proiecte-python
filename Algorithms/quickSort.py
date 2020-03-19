#l = [-1, 4, 4, 5, -2, 0, 7, -3, 8]
l = [5,4,3,0,2,1, 4.3]
#l = [12, 11, 13, 5, 6, 7]

def quickSort (arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr

    pivot = arr.pop()
    sm = []
    gr = []
    for i in arr:
        if i < pivot:
            sm.append(i)
        else:
            gr.append(i)
    return quickSort(sm) + [pivot] + quickSort(gr)

newArr = quickSort(l)
print(newArr)

