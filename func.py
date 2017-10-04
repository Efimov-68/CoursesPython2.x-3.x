'''
def myFunction(myName):
    print(123)
    print(0000)
    print('string')
    print(myName)
    print()

myFunction('Roman')

print('Hello World!')
'''
'''
def calculateTax(price, tax_rate):
    total_tax = price + (price * tax_rate)
    return total_tax

#totalTax = calculateTax(7.99, 6.99)
'''
'''
def calcTax(price, tax_rate):
    total = price + (price * tax_rate)

    my_price = 10000
    print('цена внутри функции = ', my_price)
    return total

my_price = float(input('Введите цену: '))

totalPrice = calcTax(my_price, 0.06)
print('цена = ', my_price, 'Итоговая цена = ', totalPrice)
print('цена вне функции = ', my_price)
'''
def myFunction(i):
    print('..............................................................|||||||||||')
    print('|____/\____RRRRR    OOOOO   MMM     MMM      AAA      NNN    NN\   ||   /|')
    print('|___/||\___RR  RR  OO   OO  MM M   M MM     AA AA     NN NN  NN_\  ||  /_|')
    print('|__/ || \__RRRRR   OO   OO  MM MM MM MM    AA   AA    NN  NN NN__\ || /__|')
    print('|_/  ||  \_RR  RR  OO   OO  MM  MMM  MM   AAAAAAAAA   NN   N NN___\||/___|')
    print('|/   ||   \RR   RR  OOOOO   MM       MM  AAAA   AAAA  NN    NNN____\/____|')
    print('|||||||||||..............................................................')
    print()
    print('------------------------------------------------------------------------------------------------------')
    print('|____/\____|RRRRR       AAA     BBBBB  BBBBB  IIII TTTTTT WW       WW       WW EEEEE BBBBB |\   ||   /|')
    print('|___/||\___|RR  RR     AA AA    BB  BB BB  BB  II  T TT T  WW     WWWW     WW  EE    BB  BB|_\  ||  /_|')
    print('|__/ || \__|RRRRR     AA   AA   BBBBB  BBBBB   II    TT     WW   WW  WW   WW   EEE   BBBBB |__\ || /__|')
    print('|_/  ||  \_|RR  RR   AAAAAAAAA  BB  BB BB  BB  II    TT      WW WW    WW WW    EE    BB  BB|___\||/___|')
    print('|/   ||   \|RR   RR AAAA   AAAA BBBBB  BBBBB  IIII   TT       WWW      WWW     EEEEE BBBBB |____\/____|')
    print('------------------------------------------------------------------------------------------------------')


while total <= 3:
    myFunction(i)
    i ++ 1

i = 1
total = i
