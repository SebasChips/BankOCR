from numberChecker import numberChecker

def order(numbersMatrix):
    newMatrix= []
    newRow = []
    newRow2 = []
    newRow3 = []
    addition = 0
    for i in range(1):
        for j in range(len(numbersMatrix[i])):
            addition = addition+1
            newRow.append(numbersMatrix[i][j])
            newRow2.append(numbersMatrix[i+1][j])
            newRow3.append(numbersMatrix[i+2][j])
            
            if numbersMatrix[i][j] == ' ' and numbersMatrix[i+1][j] == '|' and numbersMatrix[i+2][j] == '|':
                try:
                    if numbersMatrix[i][j+1] == ' ':
                        newMatrix.append(newRow)
                        newMatrix.append(newRow2)
                        newMatrix.append(newRow3)
                        numberChecker(newMatrix)
                        addition = 0
                        newRow = []
                        newRow2 = []
                        newRow3 = []
                        newMatrix=[]
                except IndexError:
                    if addition == 3:
                        newMatrix.append(newRow)
                        newMatrix.append(newRow2)
                        newMatrix.append(newRow3)

                        numberChecker(newMatrix)

                        addition = 0
                        newRow = []
                        newRow2 = []
                        newRow3 = []
                        newMatrix=[]
                
            elif addition == 3:
                newMatrix.append(newRow)
                newMatrix.append(newRow2)
                newMatrix.append(newRow3)

                numberChecker(newMatrix)

                addition = 0
                newRow = []
                newRow2 = []
                newRow3 = []
                newMatrix=[]