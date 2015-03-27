#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""Скрипт является парсером простых арифметических выражений."""


class Parser:
    def __init__(self, exp):
        self.exp = exp
        self.prev_token = None

        # Стек операндов (например, числа)
        self.operands = []

        # Стек операторов (функций, например +, *, и т.п.)
        self.functions = []

        self.pos = 0

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

    def execute_function(self):
        if len(self.operands) < 2:
            return

        a, b = self.operands.pop(), self.operands.pop()
        f = self.functions.pop()

        if f == '+':
            self.operands.append(b + a)
        elif f == '-':
            self.operands.append(b - a)
        elif f == '*':
            self.operands.append(b * a)
        elif f == '/':
            self.operands.append(b / a)

    def can_pop(self, c):
        if not self.functions:
            return False

        head = self.functions[-1]
        if not Parser.is_function(head):
            return False

        p1 = Parser.priority_function(c)
        p2 = Parser.priority_function(head)

        # Чем больше значение приоритета, тем меньше он
        # Например: операции * и / имеют больший приоритет, чем + и -
        return p1 >= p2

    # TODO: мне кажется, это можно и вынести из класса
    @staticmethod
    def isfloat(number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def read_number(self):
        res = ''
        point = 0

        c = self.exp[self.pos]

        while c.isdigit() or c == '.':
            if c == '.':
                point += 1
                if point > 1:
                    raise Exception('Выражение не верное -- слишком '
                                    'много точек (pos: %s)' % self.pos)

            res += c
            self.pos += 1

            c = self.exp[self.pos]

        return res

    def get_token(self):
        for i in range(self.pos, len(self.exp)):
            c = self.exp[i]

            if c.isdigit():
                return self.read_number()
            else:
                self.pos += 1
                return c

        return None

    def calculate_expression(self):
        self.pos = 0

        token = self.get_token()

        while token:
            if token != ' ':
                print('"%s", self.isfloat: %s' % (token, self.isfloat(token)))
                import time
                time.sleep(1)

            token = self.get_token()

        # for c in self.exp:
        #     if c.isspace():
        #         continue
        #
        #     elif c.isdigit():
        #         # TODO: проверять значение, ведь это может быть и int
        #         self.operands.append(float(c))
        #
        #     elif Parser.is_function(c):
        #         # Разруливаем ситуации, когда после первой скобки '(' идет знак + или -
        #         if self.prev_token and self.prev_token == '(' and (c == '+' or c == '-'):
        #             self.operands.append(0)
        #
        #         # Мы можем вытолкнуть, если оператор c имеет меньший или равный приоритет, чем
        #         # оператор на вершине стека functions
        #         # Например, с='+', а head='*', тогда выполнится операция head
        #         while self.can_pop(c):
        #             self.execute_function()
        #
        #         self.functions.append(c)
        #
        #     elif c == '(':
        #         self.functions.append(c)
        #
        #     elif c == ')':
        #         # Выталкиваем все операторы (функции) до открывающей скобки
        #         while self.functions and self.functions[-1] != '(':
        #             self.execute_function()
        #
        #         # Убираем последнюю скобку '('
        #         self.functions.pop()
        #
        #     self.prev_token = c
        #
        # if self.functions or len(self.operands) > 1:
        #     raise Exception('Неверное выражение: operands={}, functions={}'.format(self.operands, self.functions))
        #
        # # Единственным значением списка operands будет результат выражения
        # return self.operands[0]


# http://habrahabr.ru/post/50196/
# http://algolist.manual.ru/syntax/parsear.php
# http://e-learning.bmstu.ru/moodle/file.php/1/common_files/library/SPO/Compil/bmstu_iu6_Sysprogr_Compiles.pdf


# TODO: доработать: алгоритм работает только с односимвольными числами
# TODO: поддерживать вещественные числа
# TODO: завести main файл


if __name__ == '__main__':
    Parser("(10 + 2.4 * 3.1456 - 2)").calculate_expression()

    # exp = "(1 + 2 * 2 + 2)"
    # print(exp + " = " + str(Parser(exp).calculate_expression()))
    #
    # exp = "(3 + (-1 - 1))"
    # print(exp + " = " + str(Parser(exp).calculate_expression()))
    #
    # exp = "(3 + (-1 + (2 * 3 - 1) - 1))"
    # print(exp + " = " + str(Parser(exp).calculate_expression()))
