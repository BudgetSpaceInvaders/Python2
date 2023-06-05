"""def looping():
    print("Hello, world!")
    looping()


looping()"""


def push(val):
    stack.append(val)


stack = []
push(3)
push(2)
push(1)

print(stack.pop())
print(stack.pop())
print(stack.pop())
