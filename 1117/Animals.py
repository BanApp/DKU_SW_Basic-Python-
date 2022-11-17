class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "알수없음"

class Dog(Animal):
    def speak(self):
        return '멍멍!'

class Cat(Animal):
    def speak(self):
        return '야옹!'

animalList = [Dog('dog1'),Dog('dog2'),Cat('cat1')]

for i in animalList:
    print(i.name + ' : ' + i.speak())
