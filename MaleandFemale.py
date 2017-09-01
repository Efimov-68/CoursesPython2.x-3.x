male = 'm'
female = 'f'
floor = input('Если вы "мальчик" введите букву "m", а если "девочка" введите "f" ')
while floor == female:
    age = float(input('Сколько вам лет? '))
    if age >= 10 and age <= 12:
        print('Вы приняты в нашу футбольную команду девочек.')
    elif age < 10 and floor == female:
        print('Вы слишком юная, приходите в следующем году.')
    elif age > 12 and floor == female:
        print('Вы старше всех кандидаток.')
else:
    print('Мы набираем футбольную команду девочек. Спасибо за  интерес.')
