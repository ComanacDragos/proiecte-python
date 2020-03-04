def majority_element(nums):
    d = {}
    max = 0
    max_el = 0
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i] > max:
            max = d[i]
            max_el = i
    return max_el


  # Fill this in.

print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3