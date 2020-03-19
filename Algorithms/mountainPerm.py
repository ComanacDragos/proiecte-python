#n = int(input(">").strip())
n = 5
arr = []
count = 0
for i in range(0, n+1):
    arr.append(None)

def consistent(k):
    for i in range(0, k):
        #print(arr)
        if arr[k] == arr[i]:
            return False
    return True

def solution (k):
    if k == n:
        i = 0
        ok = 0
        #print(arr)
        while i < n:
            if arr[i] == n:
                ok = 1
                i += 1
            else:
                if ok == 0 and arr[i] > arr[i+1]:
                    #print("yes0")
                    return False
                if ok == 1 and arr[i] < arr[i+1]:
                    #print("yes1")
                    return False
                i += 1
        return True
    return False



def print_sol ():
    s = ""
    for i in arr:
        s += str(i)
    print(s)

def bkt(k):
    for i in range(0, n+1):
        if k == n+1:
            return
        arr[k] = i
        if consistent(k) == True:
            if solution(k) == True:
                print(arr)
                return
            else:
                bkt(k+1)

bkt(0)