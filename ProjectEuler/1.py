n = 2000000
viz = [0]*(n+1)
primes = []

while len(primes) != 10001:
    for i in range(2,n):
        if viz[i] == 0:
            viz[i] = 1
            print(i)
            primes.append(i)
            j = i+i
            while j <= n:
                viz[j] = 1
                j += i
print(primes[-1])

