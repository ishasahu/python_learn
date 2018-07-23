class Dog:
    def __init__(self, name): # self - instance of class, pass name, __  is called dunder
        print("creating instance of a dog... ")
        self._remembered_name = name  # private class variable remembered_name
        self.__private = "private membet variable"  # cas be accessed using d1.__dict__

    def bark_name(self):
        print("Bark Bark ! My name is {}".format(self._remembered_name))
    
    def set_name(self, name):
        self._remembered_name = name + 'ie'
        print("Gotcha, I will remember the new name as {}".format(self._remembered_name))

if __name__ == '__main__':
    print("Hello World")
    d1 = Dog("Pluto")
    d1.bark_name()
    d1.set_name("Pepper")
    #di.__dict__   # this will list down all the private member variables of the class
    

    
class Animal:
    def __init__(self, name, atype, age):
        self.animal_name = name
        self.animal_type = atype
        self.animal_age = age

    def getAnimal(self):
        print("The name of animal is: {}".format(self.animal_name))
        print("The type of animal is: {}".format(self.animal_type))
        print("The age of animal is: {}".format(self.animal_age))
    
a1 = Animal("Humpy", "Camel", "5")
a1.getAnimal()
    

class Cheetah:    
    def __init__(self, name, weight, speed):        
        self.name = name        
        self.weight = weight        
        self.speed = speed    
    def run_minutes(self, time):        
        distance = self.calc_distance(time)        
        miles = distance/5280        
        print('{} just traveled {} feet in {} minutes because he runs {} mph. That is {} miles.'.format(self.name, distance, time, self.speed, miles))    
    def calc_distance(self, time):        
        return ((self.speed*5280)/60)*time

# d1 = Cheetah("Chester", 150, 68)
# d1.run_minutes(18)


class Circle:
    def __int__(self, radius):
        self.radius = radius

    def calculateArea(self):
        area = 3.14 * self.radius * self.radius
        return area


class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        area = self.length * self.breadth
        return area

class Person():
    def __init__(self, name):




from collections import Counter
s = "Some String"
s = set(s)
Counter(s).most_common(s)
c = Counter(s)

letter_count = sorted(letter_count, key = lamba x:x[1]. reverse = True)

from collections import Counter
​
s = "The Zen of Python, by Tim Peters\
\
Beautiful is better than ugly.\
Explicit is better than implicit.\
Simple is better than complex.\
Complex is better than complicated.\
Flat is better than nested.\
Sparse is better than dense.\
Readability counts.\
Special cases aren't special enough to break the rules.\
Although practicality beats purity.\
Errors should never pass silently.\
Unless explicitly silenced.\
In the face of ambiguity, refuse the temptation to guess.\
There should be one-- and preferably only one --obvious way to do it.\
Although that way may not be obvious at first unless you're Dutch.\
Now is better than never.\
Although never is often better than *right* now.\
If the implementation is hard to explain, it's a bad idea.\
If the implementation is easy to explain, it may be a good idea.\
Namespaces are one honking great idea -- let's do more of those!"
​
​
letters = set(s)
counts = [s.count(i) for i in letters]
letter_count = list(zip(letters,counts))
print('Letters and their counts:' , letter_count)
print('\n\n')
letter_count = sorted(letter_count, key = lambda x:x[1], reverse = True)
print("5 most common letters:",letter_count[:6])
​
c = Counter(s).most_common(5)
print('\n\n')
print("Counter example:", c)


Collapse 