def searchMatrix(mat, value):
    if value < mat[0][0] or value > mat[-1][-1]:
        return False

    for i in mat:
        if value in range(i[0], i[-1]):
            l = 0;
            r = len(i)-1
            while l < r:

                m = (l+r)//2
                if value == i[m]:
                    return True
                elif value < i[m]:
                    r = m
                else:
                    l = m+1
            break
    return False



# Fill this in.

mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
