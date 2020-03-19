l = [2, 2, 4, 5, 6, 4, 13, 4, 10 ]

def DEI(arr, l, r):
    if l == r:
        if l%2 == 0 and arr[l]%2==0:
            return arr[l]
        return 0
    m = (l+r)//2
    return DEI(arr, l, m) + DEI(arr, m+1, r)

n = len(l)
print(n)
print(DEI(l, 0, n-1))

