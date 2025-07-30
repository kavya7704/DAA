arr = input().split()

def evaluate_postfix(arr):
    stack = []
    for token in arr:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)  # rounds toward zero
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]

print(evaluate_postfix(arr))
