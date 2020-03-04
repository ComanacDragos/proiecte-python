arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6, 7, 8, 9]

def first_sol(arr):
    aux_range = [0,0]
    mx_range = [0,0]
    arr.sort()

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == 1:
            aux_range[1] += 1
        else:
            if aux_range[1] - aux_range[0] > mx_range[1] - mx_range[0]:
                mx_range = aux_range[:]
            aux_range[0] = aux_range[1] = i
    print(mx_range)

first_sol(arr)

def second_sol (arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = False

    aux_range = [arr[0], arr[0]]
    mx_range = aux_range[:]
    for i in arr:
        aux_range=[i,i]

        while aux_range[0] in d:
            d[aux_range[0]] = True
            aux_range[0] -= 1
        aux_range[0] += 1

        while aux_range[1] in d:
            d[aux_range[1]] = True
            aux_range[1] += 1
        aux_range[1] -= 1

        if aux_range[1] - aux_range[0] > mx_range[1] - mx_range[0]:
            mx_range = aux_range[:]

    print(mx_range)

second_sol(arr)


