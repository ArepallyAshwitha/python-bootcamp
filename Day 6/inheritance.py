# inheritance
# single
class Animal():
    def speak():
        return 'Animal is speaking'
obj1=Animal
print(obj1.speak())

# multilevel
class Dog():
    def bark():
        return 'bow'
class puppy():
    def talk():
        return 'im puppy'    
obj2=Dog
print(obj2.bark())
obj3=puppy
print(obj3.talk())  

# multiple
class Father():
    def Father_speak():
        return 'Father class'
class Mother():
    def Mother_speak():
        return 'Mother class'
class kid(Father,Mother):
    def kid_speak():
        return 'im kid.im having properties to mother class to father class'
obj4=kid
print(obj4.Father_speak())    
print(obj4.Mother_speak())  
print(obj4.kid_speak())  
    
    
