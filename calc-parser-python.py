#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""Скрипт является парсером простых арифметических выражений."""


class Parser:
    def __init__(self, exp):
        self.exp = exp

    OPERATORS = {
        '+': 2,
        '-': 2,
        '*': 1,
        '/': 1,
    }

    @staticmethod
    def is_function(c):
        return c in Parser.OPERATORS.keys()

    @staticmethod
    def priority_function(c):
        if not Parser.is_function(c):
            raise Exception('Не найден оператор "{}"'.format(c))

        return Parser.OPERATORS[c]

    @staticmethod
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
            operands.append(b / a)

    @staticmethod
    def can_pop(c, function):
        if not function:
            return False

        head = function[-1]
        if not Parser.is_function(head):
            return False

        p1 = Parser.priority_function(c)
        p2 = Parser.priority_function(head)

        # Чем больше значение приоритета, тем меньше он
        # Например: операции * и / имеют больший приоритет, чем + и -
        return p1 >= p2

    def calculate_expression(self):
        # Стек операндов (например, числа)
        operands = []

        # Стек операторов (функций, например +, *, и т.п.)
        functions = []

        for c in self.exp:
            if c.isspace():
                continue

            elif c.isdigit():
                operands.append(float(c))

            elif Parser.is_function(c):
                # Разруливаем ситуации, когда после первой скобки '(' идет знак + или -
                if functions and functions[-1] == '(' and not operands and (c == '+' or c == '-'):
                    operands.append(0)

                # Мы можем вытолкнуть, если оператор c имеет меньший или равный приоритет, чем
                # оператор на вершине стека functions
                # Например, с='+', а head='*', тогда выполнится операция head
                while Parser.can_pop(c, functions):
                    Parser.execute_function(functions, operands)

                functions.append(c)

            elif c == '(':
                functions.append(c)

            elif c == ')':
                # Выталкиваем все операторы (функции) до открывающей скобки
                while functions and functions[-1] != '(':
                    # print(functions, operands)
                    Parser.execute_function(functions, operands)

                # Убираем последнюю скобку '('
                functions.pop()

        if functions or len(operands) > 1:
            raise Exception('Неверное выражение: operands={}, functions={}'.format(operands, functions))

        # Единственным значением списка operands будет результат выражения
        return operands[0]


# http://habrahabr.ru/post/50196/
# http://algolist.manual.ru/syntax/parsear.php
# http://e-learning.bmstu.ru/moodle/file.php/1/common_files/library/SPO/Compil/bmstu_iu6_Sysprogr_Compiles.pdf


# TODO: доработать: алгоритм работает только с односимвольными числами
# TODO: поддерживать вещественные числа


if __name__ == '__main__':
    # exp = "(1 + 2 * 2 + 2)"
    # print(exp + " = " + str(Parser(exp).calculate_expression()))
    #
    # exp = "(-2 + 1)"
    # print(exp + " = " + str(Parser(exp).calculate_expression()))

    # exp = "(+2 + 1 + (-1 - 1))"
    # print(exp + " = " + str(Parser(exp).calculate_expression()))

    exp = "(3 + (-1 - 1))".replace(' ', '')
    print(exp + " = " + str(Parser(exp).calculate_expression()))