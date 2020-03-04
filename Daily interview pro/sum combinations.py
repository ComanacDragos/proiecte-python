def sum_combinations_rec(l, sum, local, nums, target, aux):
    if sum == target:
        print(local)
        aux.append(local[:])
        return
    for i in range(l,len(nums)):
        if sum + nums[i] > target:
            continue

        if nums[i] == nums[i-1] and i>l:
            continue

        local.append(nums[i])
        sum_combinations_rec(i+1, sum+nums[i], local, nums, target,aux)
        local.pop()

def sum_combinations(nums, target):
    nums.sort()
    local = []
    aux = []
    sum_combinations_rec(0, 0, local, nums, target, aux)
    aux.sort(key=lambda x:x[0] < x[1])
    return aux
  # Fill this in.
#sum_combinations([10, 1, 2, 7, 6, 1, 5], 8)
#sum_combinations([1,2,2,3,4,5,6,7,8,8], 8)
#sum_combinations([1,1,1,1],4)
print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]



