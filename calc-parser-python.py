__author__ = 'ipetrash'


"""Скрипт является парсером простых арифметических выражений."""


# http://habrahabr.ru/post/50196/
# http://algolist.manual.ru/syntax/parsear.php
# http://e-learning.bmstu.ru/moodle/file.php/1/common_files/library/SPO/Compil/bmstu_iu6_Sysprogr_Compiles.pdf

# TODO: доработать: алгоритм работает только с односимвольными числами
# TODO: поддерживать вещественные числа

if __name__ == '__main__':
    def is_function(c):
        return c in ['+', '-', '*', '/']


    def priority_function(c):
        priority = {
            '+': 2,
            '-': 2,
            '*': 1,
            '/': 1,
        }

        if not c in priority:
            raise Exception('Не найден оператор "{}"'.format(c))

        return priority.get(c)


    def execute_function(functions, operands):
        if len(operands) < 2:
            return

        a, b = operands.pop(), operands.pop()
        f = functions.pop()

        if f == '+':
            operands.append(b + a)
        elif f == '-':
            operands.append(b - a)
        elif f == '*':
            operands.append(b * a)
        elif f == '/':
            operands.append(b // a)

    def can_pop(c, function):
        if not function:
            return False

        head = function[-1]
        if not is_function(head):
            return False

        p1 = priority_function(c)
        p2 = priority_function(head)

        return p1 >= p2


    exp = "(((2 + ((2 * 2) + 2 * 2)) + 2 * 3) / 2 + 3 * 2 - 4)"
    exp = "(2 + 1 * 2 + 1)"

    operands = []
    functions = []

    for c in exp:
        if c.isspace():
            continue

        elif c.isdigit():
            operands.append(int(c))

        elif is_function(c):
            while can_pop(c, functions):
                print(c, functions[-1], priority_function(c), priority_function(functions[-1]), ': ', operands)
                execute_function(functions, operands)

            functions.append(c)

        elif c == '(':
            functions.append(c)

        elif c == ')':
            # Выталкиваем все операторы (функции) до открывающей скобки
            while functions and functions[-1] != '(':
                execute_function(functions, operands)

            # Убираем последнюю скобку '('
            f = functions.pop()

    if functions or len(operands) > 1:
        raise Exception('Неверное выражение')

    print(operands)
    print(functions)
    print(exp + " = " + str(operands[0]))
