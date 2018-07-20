def countCharInSTring():
       stmt=input('Enter the String :').lower()
       x=input('Enter the letter to be counted in the above string :').lower()    
       print(stmt.count(x))


def outputExclamatedStringOrlowercaseNonExclamatedString():
       stmt=input('Enter the String :')
       if(stmt[-1]=='!'):
          print(stmt)
       else:
          print(stmt.lower())
    
def removeVowels():
       stmt=input('Enter the String :')
       vowelList=['a','e','i','o','u']
       for char in stmt:
           if char in vowelList:
               stmt=stmt.replace(char,'')
               print(stmt)

def capitalizeEveryOtherLetterInString():
       s = input('Please enter a string: ')
       for l in range(len(s)):
           if l%2 != 0:           
                s=s[0:l]+s[l].upper()+s[l+1:]
           else:
                s=s[0:l]+s[l].lower()+s[l+1:]
       print(s)


def evenList():
       s = int(input('Enter a number: '))
       print(i for i in range(s) if i%2==0)

def dividendsThatAreDivisibleByDivisor():
       s = int(input('Enter a number: '))
       d=int(input('Enter a divisor'))
       print([i for i in range(s) if i%d==0])

def intersectionOfLists():
    x=int(input('Enter a number: '))
    y=int(input('Enter max number: '))

    print([i*x for i in range(1,y) if i*x<y])

def intersectionOfListsWithUserInputs():
       list1=[]
       list2=[]
       for l1 in range(7):
           list1.append(input('enter a number for list1 :'))
       for l1 in range(7):
           list2.append(input('enter a number for list2 :'))
       print([i for i in list1 if i in list2])


def multipleOfNumber():
       x=int(input('Enter a number: '))
       y=int(input('Enter max number: '))
       
       print([i*x for i in range(1,y) if i*x<y])

def fizzBizzwithNUmbers():
    my_list = list(range(1,1001))
    i = 0
    while ( i < len(my_list)):
        if (my_list[i] % 3 == 0 or my_list[i] % 5 == 0):
            my_list[i] = 'FizzBuzz'
        elif my_list[i] % 3 == 0:
            my_list[i] = 'Fizz'
        elif my_list[i] % 5 == 0:
            my_list[i] = 'Buzz'
    print(my_list)

    l = []
    for x in range(1, 101):
       if x % 3 == 0 and x % 5 == 0:
            l.append('FizzBuzz')
       elif x % 3 == 0:
           l.append('Fizz')
       elif x % 5 == 0:
           l.append('Buzz')
       else:
           l.append(x)       
    print(l)
