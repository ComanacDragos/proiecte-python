def remove_dups(nums):
    i=1
    n=len(nums)
    while i<n:
        if nums[i] == nums[i-1]:
            nums.pop(i)
            n -= 1
        else:
            i += 1
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return len(nums)
  # Fill this in.

nums = [1, 1,13, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
# 8
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 9]

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(nums)
# 1
# [1]
