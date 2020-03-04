def maxNonAdjacentSum(nums):
    v = []
    v.append(nums[0])
    v.append(nums[1])
    global_mx = v[0]
    for i in range(2, len(nums)):
        mx = v[0]
        for j in range(1, i-1):
            if v[j] > mx:
                mx = v[j]
        v.append(mx+nums[i])
        if global_mx < v[i]:
            global_mx = v[i]
    return global_mx



# Fill this in.

print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3,1]))
# 9
# max sum is 2 (index 0) + 7 (index 3)