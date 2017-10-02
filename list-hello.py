"""for looper in [1, 2, 3, 4, 5]:
    print("hello")
print('\n')
for looper in [1, 2, 3, 4, 5]:
    print(looper)
print('\n')
for looper in [1, 2, 3, 4, 5]:
    print(looper,'* 8 =', looper * 8)
print('\n')
for looper in range(1, 5):
    print(looper, looper * 8)
print('\n')
for i in range(1, 26, 2):
    print(i, i * 2)
print('\n')
for i in range(26, 1, -2):
    print(i, i * 2)
"""

'''import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print('Start!')'''

print('Введите 3 для того, чтобы продолжить или любую другую цифру для выхода')
someInput = input()
while someInput == '3':
    print("Спасибо за 3")
    print("Введите 3 для продолжения или другое число для выхода")
    someInput = input()
print('Это не 3, вы закончили прогамму.')
