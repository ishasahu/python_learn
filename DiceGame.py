import random

def pickDices():
    diceList = ['d4','d6','d6', 'd8','d8','d8','d8','d10','d10','d12','d20','d20','d20']       
    firstThreeDices = random.sample(diceList, 3)
    print("First three dices are: ", firstThreeDices)
    for dice in firstThreeDices:
        diceList.remove(dice) 
    print("Remaining Dices to pick from: ", diceList) 
    return random.sample(diceList, 2) 

def rollDice(diceType):
    diceRange = int(diceType[1:])
    numRolled =  random.randint(1,diceRange)
    print("The dice and number rolled are: ", diceType, numRolled)
    return numRolled    

def getSumOfDices():
    dicePicked = pickDices()    
    print("The two dices picked are: ", dicePicked)
    sum = 0
    for dice in dicePicked:
        sum += rollDice(dice)
    print("The sum of number rolled in two dices is: ", sum)

getSumOfDices()