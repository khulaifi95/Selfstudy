# Dijkstra's two-stack algorithm for expression evaluation.


def is_operand(c):
    return c.isdigit()


def evaluate(expression):
    """ 
    Evaluate a given expression in prefix notation. 
    Asserts that the given expression is valid. 
    """
    stack = []

    # iterate over the string in reverse order
    for c in expression[::-1]:

        # push operand to stack
        if is_operand(c):
            stack.append(int(c))

        else:
            # pop values from stack can calculate the result
            # push the result onto the stack again
            o1 = stack.pop()
            o2 = stack.pop()

            if c == '+':
                stack.append(o1 + o2)

            elif c == '-':
                stack.append(o1 - o2)

            elif c == '*':
                stack.append(o1 * o2)

            elif c == '/':
                stack.append(o1 / o2)

    return stack.pop()


# Driver code
if __name__ == "__main__":
    test_expression = "+9*26"
    print(evaluate(test_expression))
