"""
dsi-python-fundamentals / week2 / day4-data_structures_cont / data_structures_assignment.md
"""

def generateTuplesUSingUserInputValuesSeperatedCommas():
    myStr = str(input('Enter numbers seperated by commas: ')).split(',')
    #myStr = list(input('Enter numbers seperated by commas: '))
    tupleList = [tuple((myStr[i], myStr[i+1])) for i in range(0,len(myStr)-1, 2)]
    #print(list(zip(nums[::2], nums[1::2])))  -- Other way nums is passed and int list
    print(tupleList)

def createDictWithUserInputAsKeyAndSquaredValues():
    myStr = input('Enter numbers seperated by dashes: ').split('-')
    numList = [int(i) for i in myStr]
    my_dict = {}
    for x in numList:
        my_dict[x] = x*x
    print(my_dict)

def getStatesfromDictionary():
    state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                       'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                       'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
    UInput = input('Please enter the state name: ')
    print(state_dictionary.get(UInput, 'Capital Unknown'))                  
        
def createDictUsingThreeUserInputsUntilBreak():
    while True:    
        userStr = input('Please enter a coordinate-word pair in the format (x, y, word): ').split(',') 
        if len(userStr)-1 != 0:
            myDict2 = {}            
            myDict2[tuple((userStr[0], userStr[1]))] = userStr[2]
            print(myDict2)
        else:
            break 
    while True:
        userInput = input('Please enter a coordinate to look up: ')
        if userInput == 'q':
            break
        else:            
            print(myDict2.get(tuple(userInput.split(',')), 'Coordinates not found'))          


def printCommonNumbersfromUSerInputs():
    set1 =set(input('Print first set of comma seperated number: ').split(','))
    set2 = set(input('Print second set of comma seperated number: ').split(','))
    print(set1.intersection(set2))

def printUniqueWordfromUserInputSet():
    set3 = {str(s1) for s1 in input('Print set of comma seperated words: ').split(',')}
    print(','.join(set3))     

def getaWordSetfromUSer():
    wordset = set()
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        elif word == 'v':
            print(' '.join(wordset))
        else:
            wordset.add(word)
            
    
