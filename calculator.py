import fire


class Calculator(object):
    """A simple calculator."""

    def help(self):
        return "\nиспользование 'действие' 'число 1' 'число 2'\n\n minus - вычесть второе число из первого\n plus - сложить два числа\n multiply - перемножить два числа\n divide - разделить первое число на второе\n"

    def double(self, number):
        return 2 * number
    def minus(self, number1, number2):
        return number1 - number2
    def plus(self, number1, number2):
        return number1 + number2
    def multiply(self, number1, number2):
        return number1 * number2
    def divide(self, number1, number2):
        return number1 / number2


if __name__ == '__main__':
    fire.Fire(Calculator)
