fin = open("scmax.in", "r")
fout = open("scmax.out", "w")
lines = fin.readlines()
arr = lines[1].split()
#arr = [2, 12, 3, 6, 14, 3 ,4, 7,2] # --->  12 6 4 2

def LDS (arr):
    v = []
    daddys = [-1]
    v.append(1)
    i = 1

    while i < len(arr):


        mx_len = 0
        mx_daddy = -1
        for j in range(0, i):
            if int(arr[j]) < int(arr[i]) and mx_len < v[j]:
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
    fout.write(str(len(seq)) + "\n")
    s = ""
    for i in seq:
        s += str(i)
        s += " "
    fout.write(s)
    for i,j in zip(v, daddys):
        print(v[i], daddys[j])

LDS(arr)

