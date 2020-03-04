def consistent(nums, v, target):
    last = v[-1]
    for i in range(len(v)-1):
        if v[i] >= last:
            return False
    s = 0
    for i in v:
        s += nums[i]
    if s <= target:
        return True
    return False


def valid(nums, v, target):

    s = 0
    for i in v:
        s += nums[i]
    if s == target:
        return True
    return False


def bkt(nums, x, target, res):
    x.append(0)
    for i in range(len(nums)):
        x[-1] = i
        if consistent(nums, x, target):
            if valid(nums, x, target):
                arr = [nums[el] for el in x]
                arr.sort()
                

                res.append(arr)
                #res.append(x)
            else:
                bkt(nums, x[:], target, res)

def sum_combinations(nums, target):
    res = []
    x = []
    bkt(nums, x, target, res)
    return res

  # Fill this in.


res = sum_combinations([10, 1, 2, 7, 6, 1, 5], 8)



for i in res:
    print(i)
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
# 1 1 2 5 6 7

