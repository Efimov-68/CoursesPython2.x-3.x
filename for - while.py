#for table
'''result = int(input("Введите число:\n"))
for i in range(0, 11):
    print(result, 'x ', i, '=', result * i)'''

#while table
'''total = 0
result = int(input('Введите значение: '))
print('Таблица:')
while total < 11:
    print(result, 'x', total, '=', result*total)
    total += 1'''

#for с произвольным порядком
'''result = int(input('Введите значение: '))
x = int(input('Введите до какого значения: '))
x += 1
print('Ваша таблица:')
for i in range(x):
    print(result, 'x', i, '=', result*i)'''

#while с произвольным порядком
result = int(input('Введите значение: '))
x = int(input('Введите до какого значения: '))
i = 0
while i <= x :
    print(result, 'x', i, '=', result*i)
    i += 1
