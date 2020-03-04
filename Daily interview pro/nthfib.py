fib = {0: 0,
       1: 1}

def getNthFib(n):
    if n in fib:
        return fib[n]

    fib[n] = getNthFib(n-1) + getNthFib(n-2)
    return fib[n]

print(getNthFib(990) == 353410009178752575339944833520459068284945046358154977604109175253890696634271360121583566110064725510836075851584985143412396868586425109102723291106570618750075392710633321729992106743321640281356794177320)
