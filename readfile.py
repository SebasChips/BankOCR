from orderMatrix import order

def readTextFile():
    textfile = open('numbers.txt', 'r')
    numbersMatrix= []  
    row=[]
    while 1:
        char = textfile.read(1)

        if char != "\n":
            row.append(char)
        else:
            numbersMatrix.append(row)
            row = []

        if not char:
            break


    textfile.close()
    order(numbersMatrix) 