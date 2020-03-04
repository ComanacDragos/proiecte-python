def one_bits(num):
    s = 0
    while num != 0:
        s += num & 1
        num = num >> 1
    return s
  # Fill this in.

print(one_bits(7))
# 4
# 23 = 0b1011
