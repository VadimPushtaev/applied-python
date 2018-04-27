from command_pool import CommandPool
from command_handler import CommandHandler


@CommandPool.register_command_class
class CalcCommandHandler(CommandHandler):
    def handle(self, text):
        command_name = 'calc '
        if text.startswith(command_name):
            expression = text[len(command_name):].replace(' ', '')
            priorities = {'*': 1, '/': 1, '-': 0, '+': 0}
            element = '0'
            operands = []
            operators = []

            def calculate():
                operator = operators.pop()
                right_operand = operands.pop()
                left_operand = operands.pop()
                if operator == '+':
                    result = left_operand + right_operand
                elif operator == '-':
                    result = left_operand - right_operand
                elif operator == '*':
                    result = left_operand * right_operand
                elif operator == '/':
                    result = left_operand / right_operand
                operands.append(result)

            for symbol in expression:
                if symbol in r'+-*()/':
                    if element != '0':
                        operands.append(float(element))
                        if (len(operators) > 0) and (priorities[operators[-1]] > priorities[symbol]):
                            calculate()
                        element = '0'
                    operators.append(symbol)
                elif ('0' <= symbol <= '9') or (symbol == '.'):
                    element += symbol
                else:
                    raise SyntaxError
            if element != '0':
                operands.append(float(element))
            while(len(operators) > 0):
                calculate()
            return operands[0]
