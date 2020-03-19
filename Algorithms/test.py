def f(n):
    '''
    computes the sum of the digits
    :param n: natural number
    :return: sum of all digits of n
    '''
    if n <= 0:
        raise ValueError()
    l = []
    while n > 0:
        c = n%10
        n = n//10
        l.append(c)
    for i in range(len(l)-1):
        l[i+1] += l[i]
    return l[-1]

def test():
    try:
        f(-1)
        assert False
    except ValueError:
        assert True

    for i in range(1, 10):
        assert f(i) == i

    assert f(12345) == 15
    assert f(1000000) == 1


f = open("test.txt", "a")
f.write("\nline3")
f.close()