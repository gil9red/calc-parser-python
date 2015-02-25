__author__ = 'ipetrash'


"""Скрипт является парсером простых арифметических выражений."""


# http://habrahabr.ru/post/50196/
# http://algolist.manual.ru/syntax/parsear.php
# http://e-learning.bmstu.ru/moodle/file.php/1/common_files/library/SPO/Compil/bmstu_iu6_Sysprogr_Compiles.pdf

if __name__ == '__main__':
    # def is_function(c):
    #     return c in ['+', '-', '*', '/']
    #
    #
    # def priority_function(c):
    #     priority = {
    #         '+': 1,
    #         '-': 1,
    #         '*': 2,
    #         '/': 2,
    #     }
    #
    #     if not c in priority:
    #         raise Exception('Не найден оператор "{}"'.format(c))
    #
    #     return priority.get(c)


    exp = "(2 + (2 + 3 + 1) - 4)"

    operands = []
    functions = []

    for c in exp:
        if c.isspace():
            continue

        elif c.isdigit():
            operands.append(int(c))

        elif c in ['+', '-']:
        # elif is_function(c):
            functions.append(c)

        elif c == '(':
            functions.append(c)

        elif c == ')':
            f = functions.pop()

            # Выталкиваем все операторы (функции) до открывающей скобки
            while f != '(':
                a, b = operands.pop(), operands.pop()

                if f == '+':
                    operands.append(b + a)
                elif f == '-':
                    operands.append(b - a)

                f = functions.pop()


    print(exp + " = " + str(operands[0]))
