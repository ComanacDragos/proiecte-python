arr = [2, 12, 3, 6, 14, 3 ,4, 7,2] # --->  12 6 4 2

def LDS (arr):
    v = []
    daddys = [-1]
    if arr[0]%2 == 0:
        v.append(1)
    else:
        v.append(0)
    i = 1

    while i < len(arr):

        if arr[i] % 2 == 1:
            v.append(0)
            daddys.append(-1)

        else:
            mx_len = 0
            mx_daddy = -1
            for j in range(0, i):
                if arr[j] > arr[i] and mx_len < v[j]:
                    mx_len = v[j]
                    mx_daddy = j

            v.append(mx_len+1)
            daddys.append(mx_daddy)

        i += 1
    mx = v[0]
    mx_poz = 0
    for i in range(1,len(arr)):
        if mx < v[i]:
            mx = v[i]
            mx_poz = i

    poz = mx_poz
    seq = []
    while poz != -1:
        seq.append(arr[poz])
        poz = daddys[poz]

    seq.reverse()
    print(seq)

LDS(arr)

