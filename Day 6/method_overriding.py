# method overriding
class Animal():
    def speak():
        return 'speak'
class Dog(Animal):
    def speak():
        return 'dog is speaking'
class Puppy(Dog):
    def speak():
        return 'im puppy..' 
obj3=Puppy
print(obj3.speak())           