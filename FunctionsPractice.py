#https://github.com/gSchool/dsi-python-fundamentals/blob/master/week3/day5-intro_to_functions/hard_functions_assignment.md

def factorial(num):        
    i = 1
    factorial = 1
    while i <= num and num != 0:
        factorial = factorial*i
        i = i+1
    return factorial

def isPrime(n): 
    i = 1   
    for i in range(2, n+1):
        if n%i == 0: 
            break           
    if i == 1 or i == n:
        return True
    else:
        return False

def countWords(myStr):
    myList = myStr.split(' ')
    print(len(myList))


def countDelimitedWords(myStr, delimiter= ' '):
    myList = myStr.split(delimiter)
    print(len(myList))

def countLengthofWords(myStr, delimiter= ' '):
    lenList = myStr.split(delimiter)
    countList = [len(x) for x in lenList]
    return countList


def prime(n):
    pList = []
    for i in range(1, n+1): 
        if isPrime(i):
            pList.append(i)
    return pList

def checkListDivisibilty(myList, divisor):
    newList = []
    for i in myList:
        if i%divisor == 0:
            newList.append('yes')
        else:
            newList.append('no')
    return newList

def checkLetterinStringList(myList, string):
    newList = []
    for s in myList:
        if s[-1] == string:
            newList.append(s)
    return newList

def getIndexinString(myList, string):
    # Uncool way       
    newList = []
    for index, s in enumerate(myList):
        if string in s:
            newList.append(index)
    return newList
    

def getIndexinStringCoolWay(myList, string):
    # Cool way 
    return[idx for idx, word in enumerate(myList) if string in word]

def calculateTaxesWithSortedTupleList(tupleListSortedForTAXCalc, income):
    tax = 0
    for taxBracket in tupleListSortedForTAXCalc:
        if income >= taxBracket[0]:
            tax += taxBracket[0] * taxBracket[1]
            income = income - tax
        else: 
            continue
    return tax
        
            
def calculateTaxesWithUnsortedTupleList(tupleListUnsortedForTAXCalc, income):
    tax = 0
    tupleListSortedForTAXCalc = sorted(tupleListUnsortedForTAXCalc, key=lambda tup: tup[0])
    tax = calculateTaxesWithSortedTupleList(tupleListSortedForTAXCalc, income)
    return tax
    


# Tic-Tac-Toe problem - Lakshmi
# https://github.com/gSchool/dsi-python-fundamentals/blob/master/week3/day6-functions_practice/assignments/hard_functions_assignment.md






