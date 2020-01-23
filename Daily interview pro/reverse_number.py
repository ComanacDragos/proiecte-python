def reverse_integer(num):
    sign = num//abs(num)
    num = abs(num)
    reverse = num % 10
    num = num // 10
    while num != 0:
        reverse = reverse * 10 + num %10
        num = num // 10

    reverse *= sign
    return int(reverse)

print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123


x = [5, "asd", 4]

for i, el in enumerate(x):
    print(i , "->", el)