#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""Скрипт является парсером простых арифметических выражений."""


OPERATORS = {
    '+': 2,
    '-': 2,
    '*': 1,
    '/': 1,
}


def is_function(c):
    return c in OPERATORS.keys()

def priority_function(c):
    if not is_function(c):
        raise Exception('Не найден оператор "{}"'.format(c))

    return OPERATORS[c]

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

def can_pop(c, function):
    if not function:
        return False

    head = function[-1]
    if not is_function(head):
        return False

    p1 = priority_function(c)
    p2 = priority_function(head)

    # Чем больше значение приоритета, тем меньше он
    # Например: операции * и / имеют больший приоритет, чем + и -
    return p1 >= p2


# http://habrahabr.ru/post/50196/
# http://algolist.manual.ru/syntax/parsear.php
# http://e-learning.bmstu.ru/moodle/file.php/1/common_files/library/SPO/Compil/bmstu_iu6_Sysprogr_Compiles.pdf


# TODO: доработать: алгоритм работает только с односимвольными числами
# TODO: поддерживать вещественные числа
# TODO: разруливать ситуации, когда после первой скобки '(' идет знак + или -
# // разруливаем унарный + и -
#    if (prevToken == "("
#       && (token == "+" || token == "-"))
#         operands.push("0"); // Добавляем нулевой элемент


def calculate_expression(exp):
    # Стек операндов (например, числа)
    operands = []

    # Стек операторов (функций, например +, *, и т.п.)
    functions = []

    for c in exp:
        if c.isspace():
            continue

        elif c.isdigit():
            operands.append(float(c))

        elif is_function(c):
            # Мы можем вытолкнуть, если оператор c имеет меньший или равный приоритет, чем
            # оператор на вершине стека functions
            # Например, с='+', а head='*', тогда выполнится операция head
            while can_pop(c, functions):
                execute_function(functions, operands)

            functions.append(c)

        elif c == '(':
            functions.append(c)

        elif c == ')':
            # Выталкиваем все операторы (функции) до открывающей скобки
            while functions and functions[-1] != '(':
                execute_function(functions, operands)

            # Убираем последнюю скобку '('
            functions.pop()

    if functions or len(operands) > 1:
        raise Exception('Неверное выражение: operands={}, functions={}'.format(operands, functions))

    # Единственным значением списка operands будет результат выражения
    return operands[0]


if __name__ == '__main__':
    exp = "(((2 + ((2 * 2) + 2 * 2)) + 2 * 3) / 2 + 3 * 2 - 4)"
    print(exp + " = " + str(calculate_expression(exp)))

    exp = "(2 + 1 * 2 + 1)"
    print(exp + " = " + str(calculate_expression(exp)))

    exp = "(2 * 1 * 2 / 1 / 2 * 2 * 2 / (4 + 2))"
    print(exp + " = " + str(calculate_expression(exp)))
