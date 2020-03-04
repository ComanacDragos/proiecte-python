def find_num(nums, target):
    left = -1
    right = -1
    for i in range(len(nums)):
        if nums[i] == target:
            left = i
            break
    if left == -1:
        return (-1,-1)

    for j in range(len(nums)-1, 0, -1):
        if nums[j] == target:
            right = j
            break

    return (left,right)


  # Fill this in.

print(find_num([1, 4, 3, 1, 7], 1))
# (0, 1)

print(find_num([1, 2, 3, 4], 5))
# (-1, -1)