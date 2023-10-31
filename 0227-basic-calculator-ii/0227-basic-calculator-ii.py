class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op == '+': stack.append(num)
            elif op == '-': stack.append(-num)
            elif op == '*': stack.append(stack.pop() * num)
            elif op == '/': 
                n = stack.pop()
                if n < 0: stack.append(-(-n // num))
                else: stack.append(n // num)

        stack = []
        num = 0
        pre_op = '+'

        for c in s.replace(" ",""):
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in '+-*/':
                update(pre_op, num)
                num = 0
                pre_op = c
        
        update(pre_op, num)
        print(stack)
        return sum(stack)