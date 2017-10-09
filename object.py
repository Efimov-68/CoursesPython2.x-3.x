#####
'''
class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = 'Привет, я ' + self.size + ' ' + self.color + ' мяч.'
        return msg
        
    def bounce(self):
        if self.direction == 'вниз':
            self.direction = 'вверх'
        

myBall = Ball('желтый','большой','вниз')

print('Я только что создал мяч.')
print('Размер моего мяча', myBall.size)
print('Цвет моего мяча',myBall.color)
print('Мой мяч движется', myBall.direction)
print('Сейчас я поменяю направление движения мяча')
print('')
myBall.bounce()
print('Теперь мяч движется', myBall.direction)
print(myBall)
'''
#####
'''
class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "сырая"
        self.condiments = []

    def __str__(self):
        msg = 'сосиска'
        if len(self.condiments) > 0:
            msg = msg + ' c '
        for i in self.condiments:
            msg = msg + i + ', '
        msg = msg.strip(', ')
        msg = self.cooked_string + ' ' + msg + '.'
        return msg

    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = 'Сгоревшая'
        elif self.cooked_level > 5:
            self.cooked_string = 'Хорошо прожаренная'
        elif self.cooked_level > 3:
            self.cooked_string = 'Средней прожарки'
        else:
            self.cooked_string = 'Сырая'

    def addCondiment(self, condiment):
        self.condiments.append(condiment)

myDog = HotDog()
print(myDog)
print('Готовим сосиску еще 4 минуты...')
myDog.cook(4)
print(myDog)
print('Готовим сосиску еще 3 минуты...')
myDog.cook(3)
print(myDog)
print('Готовим сосиску еще 10 минут?')
myDog.cook(10)
print(myDog)
print('Сейчас я добавлю в хот-дог другие компоненты')
myDog.addCondiment('кетчуп')
myDog.addCondiment('горчица')
print(myDog)
'''
#####
'''
class GameObject:
    def __init__(self, name):
        self.name = name

    def pickUp(self, player):
        pass
        # код добавляющий объекты
        # в коллекцию игрока

class Coin(GameObject):
    def __init__(self, value):
        GameObject.__init__(self, 'монетка')
        self.value = value

    def spend(self, buyer, seller):
        pass
        # Сюда поместим код, удаляющий монетку
        # из денег покупателя и
        # добавляющий ее к деньгам продавца
'''
#####

class BankAccount:
    def __init__(self, name, number, total):
        self.acc_name = name
        self.acc_num = int(number)
        self.acc_tot = float(total)
        
    '''
    def __str__(self):
        pass
    def account(self,):
        pass
    '''

myBankAccount = BankAccount('ЦБ Банк', 3333000000000000, 1278899.58)

print('Наименование Банка:', myBankAccount.acc_name)
print('Номер счета:', myBankAccount.acc_num)
print('Состояние счета:', myBankAccount.acc_tot)
print()
