'''
# Задание 1
# Имена должны сохраняться в списке и выводиться в конце программы.
# Запрос от пользователя
name_1 = input('Введите 5(пять) имен (после каждого нажатия Enter):\nИмя №1: ')
name_2 = input('Имя №2: ')
name_3 = input('Имя №3: ')
name_4 = input('Имя №4: ')
name_5 = input('Имя №5: ')

# Создание списка
name_list = [name_1, name_2, name_3, name_4, name_5]

# Вывод введенной инфорации
print('Это имена: ', name_list)

###### Конец программы
'''
'''
# Задание 2
# Измените программу из предыдущего задания, сделав так, чтобы она выводила на
# экран как исходный, так и отсортированный список.
name_1 = input('Введите 5(пять) имен (после каждого нажатия Enter):\nИмя №1: ')
name_2 = input('Имя №2: ')
name_3 = input('Имя №3: ')
name_4 = input('Имя №4: ')
name_5 = input('Имя №5: ')

name_list = [name_1, name_2, name_3, name_4, name_5]

print('Это имена: ', name_list, ';', sorted(name_list))

# Конец программы
'''
#####
'''
# Задание 3
#Еще раз измените программу, чтобы она выводила на экран только третье из вве-
# денных имен:
name_1 = input('Введите 5(пять) имен (после каждого нажатия Enter):\nИмя №1: ')
name_2 = input('Имя №2: ')
name_3 = input('Имя №3: ')
name_4 = input('Имя №4: ')
name_5 = input('Имя №5: ')

name_list = [name_1, name_2, name_3, name_4, name_5]

print('Третье введенное имя: ', name_list[2])
# Конец программы
'''
#####
'''
# Задание 4
# И еще раз модифицируйте программу, предоставив пользователю возможность
# заменять одно из имен. Сначала он должен указать, какое имя нужно заменить,
# а потом ввести новое имя. В конце программы выведите новый список на экран:
name_1 = input('Введите 5(пять) имен (после каждого нажатия Enter):\nИмя №1: ')
name_2 = input('Имя №2: ')
name_3 = input('Имя №3: ')
name_4 = input('Имя №4: ')
name_5 = input('Имя №5: ')

name_list = [name_1, name_2, name_3, name_4, name_5]

print('', name_list)

old_name = name_list.remove(input('Введите имя для удаления: '))
new_name = name_list.append(input('Введите новое имя: '))

print(name_list)
# Конец программы
'''
#####

# Задание 5
# Напишите словарь, который даст пользователю возможность вводить слова и их
# определения, а затем искать их. Убедитесь, что пользователю сообщается об от-
# сутствии слова в словаре. После запуска программа должна работать так:

confirmation = input('Добавить или искать слово(y/n): ')
if confirmation == 'y':
    name_key = input('Введите слово: ')
    name_value = input('Введите определение: ')
    my_dict = {name_key: name_value}
    print('Слово добавлено!')
elif confirmation == 'n':
    search_key = input('Введите слово для поиска: ')
    if search_key in my_dict:
        print(my_dict[search_key])
    else:
        my_dict(search_key) != True
        print('Данного слова нет в словаре')