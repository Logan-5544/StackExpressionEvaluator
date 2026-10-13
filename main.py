class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)


# Operator precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return 0


# Calculation function
def calculate(a, b, op):
    if op == '+':
        return a + b

    elif op == '-':
        return a - b

    elif op == '*':
        return a * b

    elif op == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")

    else:
        raise ValueError("Invalid operator")


# Evaluate expression
def evaluate_expression(expression):
    numbers = Stack()
    operators = Stack()

    tokens = expression.split()

    for token in tokens:

        # If token is a number
        if token.isdigit():
            numbers.push(int(token))

        # Opening parenthesis
        elif token == '(':
            operators.push(token)

        # Closing parenthesis
        elif token == ')':

            while (not operators.is_empty()
                   and operators.peek() != '('):

                op = operators.pop()
                b = numbers.pop()
                a = numbers.pop()

                result = calculate(a, b, op)
                numbers.push(result)

            if not operators.is_empty():
                operators.pop()  # Remove '('

        # Operator
        elif token in ['+', '-', '*', '/']:

            while (
                not operators.is_empty()
                and operators.peek() != '('
                and precedence(operators.peek()) >= precedence(token)
            ):
                op = operators.pop()

                b = numbers.pop()
                a = numbers.pop()

                result = calculate(a, b, op)
                numbers.push(result)

            operators.push(token)

    # Evaluate remaining operators
    while not operators.is_empty():

        op = operators.pop()

        b = numbers.pop()
        a = numbers.pop()

        result = calculate(a, b, op)
        numbers.push(result)

    return numbers.pop()


# Read expressions from input file
def read_expressions(filename):
    with open(filename, 'r') as file:

        content = file.read()

    expressions = []

    for line in content.splitlines():

        line = line.strip()

        if line and line != "-----":
            expressions.append(line)

    return expressions


# Write results to output file
def write_results(filename, results):

    with open(filename, 'w') as file:

        for i, result in enumerate(results):

            # Remove .0 when result is a whole number
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            file.write(str(result) + '\n')

            if i < len(results) - 1:
                file.write("-----\n")


# Main program
def main():

    expressions = read_expressions('input.txt')

    results = []

    for expression in expressions:

        result = evaluate_expression(expression)

        results.append(result)

    write_results('output.txt', results)

    print("Expressions evaluated successfully.")
    print("Check the output.txt file for results.")


# Start the program
if __name__ == "__main__":
    main()