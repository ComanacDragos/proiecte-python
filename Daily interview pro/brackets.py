def generate_brackets(n):
    brackets = ['()']
    for i in range(1,n):
        n = len(brackets)
        for j in range(n):
            s = "()" + brackets[j]
            brackets.append(s)

            s = brackets[j] + "()"
            brackets.append(s)

        for j in range(i):
            brackets[j] = "("+str(brackets[j])+")"
        brackets.pop()
    return brackets


# Fill this in.

print(generate_brackets(1))
# ['()']

print(generate_brackets(4))
# ['((()))', '(()())', '()(())', '()()()', '(())()']