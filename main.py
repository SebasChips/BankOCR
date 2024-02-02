from readfile import readTextFile
from checkingAccount import check
from numberChecker import numbers
import os

def saveBankAccount(numbers, checkAccount):
    if os.path.exists("bankAccounts.txt"):
        modo = 'a'
    else:
        modo = 'w'

    with open('bankAccounts.txt', modo) as file:
        file.write(" ".join(map(str, numbers)))
        file.write(f" {checkAccount}\n")

readTextFile()
checkAccount = check(numbers)


if checkAccount == "OK":
    saveBankAccount(checkAccount, numbers)
elif checkAccount == "ILL":
    saveBankAccount(checkAccount, numbers)
elif checkAccount == "ERR":
    saveBankAccount(checkAccount, numbers)



