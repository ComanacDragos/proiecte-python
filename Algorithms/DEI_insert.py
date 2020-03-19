def DEI (arr, l, r, index, val):
    if l <= r:
        m = (l+r)//2
        #print(l, r, arr[m], index)

        if m == index:
            arr.append(None)
            for i in range(len(arr)-2, m-1, -1):
                #print(i)
                arr[i+1] = arr[i]
            arr[m] = val


        if index < m:
            return DEI(arr, l, m - 1, index, val)
        else:
            return DEI(arr, m + 1, r, index, val)
    else:
        return -1

l = [5,23,4,67,22,3]
l.sort()
print(l)
DEI(l, 0,len(l)-1,6, 66)
print(l)