numbers= []
def numberChecker(newMatrix):
    if newMatrix == number0:
        numbers.append(0)
    elif newMatrix == number1:
        numbers.append(1)
    elif newMatrix == number2:
        numbers.append(2)
    elif newMatrix == number3:
        numbers.append(3)
    elif newMatrix == number4:
        numbers.append(4)
    elif newMatrix == number5:
        numbers.append(5)
    elif newMatrix == number6:
        numbers.append(6)
    elif newMatrix == number7:
        numbers.append(7)
    elif newMatrix == number8:
        numbers.append(8)
    elif newMatrix == number9:
        numbers.append(9)
    else: numbers.append('?')

number0 = [[' ', '_', ' '], ['|', ' ', '|'], ['|', '_', '|']]
number1 = [[' '], ['|'], ['|']]
number2 = [[' ', '_', ' '], [' ', '_', '|'], ['|', '_', ' ']]
number3 = [[' ', '_', ' '], [' ', '_', '|'], [' ', '_', '|']]
number4 = [[' ', ' ', ' '], ['|', '_', '|'], [' ', ' ', '|']]
number5 = [[' ', '_', ' '], ['|', '_', ' '], [' ', '_', '|']]
number6 = [[' ', '_', ' '], ['|', '_', ' '], ['|', '_', '|']]
number7 = [[' ', '_', ' '], [' ', ' ', '|'], [' ', ' ', '|']]
number8 = [[' ', '_', ' '], ['|', '_', '|'], ['|', '_', '|']]
number9 = [[' ', '_', ' '], ['|', '_', '|'], [' ', '_', '|']]