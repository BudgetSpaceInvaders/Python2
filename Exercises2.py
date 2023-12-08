"""
par_ord = ("()", "[]", "{}")
s = '()[]{}'


def par_checker(s):
    end = len(s) - 1
    for x in range(end):
        if par_ord[0] in s or par_ord[1] in s or par_ord[2] in s:
            print("The parentheses are ordered properly!")
        else:
            print("There are no parentheses, or they aren't close properly, or they aren't in order!")

par_checker(s)"""


def isvalid(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif c == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        elif c == ']' and len(stack) > 0 and stack[-1] == '[':
            stack.pop()
        elif c == '}' and len(stack) > 0 and stack[-1] == '{':
            stack.pop()
        else:
            return False
    return len(stack) == 0


print(isvalid("(])[{}"))
