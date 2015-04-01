# calc-parser-python
Математический парсер простых выражений (#python #python3 #calc #parser)

##### Пример:
###### >>> from calc_parser import Parser
###### >>> Parser("(10 + 2.4 * 3.1456 - 2)").calc()
###### 15.54944
###### >>> Parser("(1 + 2 * 2 + 2)").calc()
###### 7
###### >>> Parser("(3 + (-1 - 1))").calc()
###### 1
###### >>> Parser("(3 + (-1 + (2 * 3 - 1) - 1))").calc()
###### 6
###### >>> Parser("(2 ^ 3 + 2 + 3 ^ 2 + 1)").calc()
###### 20
