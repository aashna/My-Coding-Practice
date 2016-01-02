def evaluatePostfix(expression):
    stack = []

    if expression.isalnum():
        return expression

    expression = expression.split()

    for char in expression:
        print stack
        if char.isdigit():
            stack.append(float("{0:.5f}".format(float(char))))
        else:
            if not stack:
               return ' '.join(expression)
            second = stack.pop()
            first = stack.pop()

            if char == '+':
                stack.append(float("{0:.5f}".format(first+second)))
            elif char == '-':
                stack.append(float("{0:.5f}".format(first-second)))
            elif char == '*':
                stack.append(float("{0:.5f}".format(first*second)))
            elif char == '/':
                stack.append(float("{0:.5f}".format(first/second)))


    return "{0:.5f}".format(stack.pop())

#print evaluatePostfix('A2')
line = raw_input("Enter rows and cols: ") 
cols= int(line[0])
rows = int(line[2])

for _ in range(rows*cols):
    cell=raw_input()
    print evaluatePostfix(cell)