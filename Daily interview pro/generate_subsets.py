def consistent (v):
    if len(v) == 0:
        return True
    last = v[-1]
    for i in range(len(v)-1):
        if v[i] >= last:
            return False
    return True

def bkt (nums, v, aux):
    v.append(0)
    for i in range(1, len(nums)+1):
        v[-1] = i
        #print(v)
        if consistent(v):
            if len(v) <= len(nums):
                aux.append(v[:])
                bkt(nums, v, aux)
                v.pop()

def generateAllSubsets(nums):
    aux = [[]]
    v = []
    bkt(nums, v, aux)
    return aux
  # Fill this in.

print(generateAllSubsets([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
