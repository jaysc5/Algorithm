class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+' : lambda a, b: a + b, '-' : lambda a, b: a - b, '*' : lambda a, b: a * b, '/' : lambda a, b: int(a / b)}
        stack = []

        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[t](a, b))
            else:
                stack.append(int(t))

        return stack.pop()