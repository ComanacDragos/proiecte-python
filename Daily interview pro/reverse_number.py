def reverse_integer(num):
    sign = num//abs(num)
    num = abs(num)
    reverse = num % 10
    num = num // 10
    while num != 0:
        reverse = reverse * 10 + num %10
        num = num // 10

    reverse *= sign
    return int(reverse)

#print(reverse_integer(135))
# 531

#print(reverse_integer(-321))
# -123

"""
x = [5, "asd", 4]

for i, el in enumerate(x):
    print(i , "->", el)


def f (a):

    a = [1,2]
    print(id(a))
    a [1]=5
a = [1,2,3]
print(id(a))
f (a)
print(a)
"""



class A:
    def __init__(self, var2):
        self.var = 0
        self.var2 =var2

a1 = A(0)
a2 = A(0)

a1.var += 1
a1.var2 += 2

a2.var += 1
a2.var2 += 3

print(a1.var, a1.var2)

print(a2.var, a2.var2)

