'''
# класс родитель
class Father():

    def family(self):
        print('Hello! I am Father Family.')

# класс наследник
class Son(Father):

    def family(self):
        Father.family(self)
        print('Hi! I am a Son')


# Объекты
myFather = Father()
mySon = Son()
# Экземпляры
myFather.family()
mySon.family()
'''


class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = 'Doctor ' + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ', Esquire'

    def test(self):
        print('HIHIHIHIHI')

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


person = Person('Fudd')
doctor = MDPerson('Nad')
lawyer = JDPerson('Arni')
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(person.name)
print(doctor.name)
print(lawyer.name)
lawyer.test()
print(bob.name)
print(bob.email)
