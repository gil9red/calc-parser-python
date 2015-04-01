#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


if __name__ == '__main__':
    from calc_parser_python import Parser


    exp = "(10 + 2.4 * 3.1456 - 2)"
    print(exp + " = " + str(Parser(exp).calculate_expression()))

    exp = "(1 + 2 * 2 + 2)"
    print(exp + " = " + str(Parser(exp).calculate_expression()))

    exp = "(3 + (-1 - 1))"
    print(exp + " = " + str(Parser(exp).calculate_expression()))

    exp = "(3 + (-1 + (2 * 3 - 1) - 1))"
    print(exp + " = " + str(Parser(exp).calculate_expression()))
