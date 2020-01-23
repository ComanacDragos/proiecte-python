def reshape_matrix (matrix, c, r):
    new_matrix = []

    for i in range (0, r):
        l = []
        for j in range (0,c):
            l.append(None)
        new_matrix.append(l)

    if len(matrix) * len(matrix[0]) != r*c:
        return None

    i = 0
    j = 0
    for p in matrix:
        for q in p:
            new_matrix[i][j] = q
            j += 1
            if j == c:
                i += 1
                j = 0
    return new_matrix

#print(reshape_matrix([[1, 2], [3, 4]], 4, 1))
# [[1], [2], [3], [4]]

#rint(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None



class A:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return str(self.name) + " " + str(self.price)

p1 = A("name1",1)
p2 = A("name2",2)


l = [p1, p2]


aux = p1
p1 = p2
p2 = aux

print(p1)
print(p2)



arr = [15, 27, 14, 38, 63, 55, 46, 65, 85, 45]

def lds (arr):
    v = []
    for i in range(len(arr)):
        v.append(0)
    mx = 1
    v[0] = 1
    for i in range(1, len(arr)):
        mx_len = 0
        for j in range (0, i):
            if arr[i] < arr[j]:
                if mx_len < v[j]:
                    mx_len = v[j]

        if mx_len == 0:
            v[i] = 1
        else:
            v[i] = mx_len + 1

        if mx < v[i]:
            mx = v[i]

    return mx

print(lds(arr))

#a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]

a = [-2, -3, 4, -1, -2, 1, 5, -3]
def max_sum (arr):
    v = []
    for i in range(0, len(arr)):
        v.append(0)

    mx = arr[0]
    v[0] = arr[0]

    for i in range(1, len(arr)):
        pass
