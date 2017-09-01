import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print('Попробуй угадать число от 1 до 99')
while guess != secret and tries < 6:
    guess = int(input('Ваш вариант: '))
    if secret < guess:
        print('Это число слишком большое! Попробуй еще.')
    elif secret > guess:
        print('Это слишком маленькое число! Попробуй еще.')
    tries+=1
if guess == secret:
    print('Вы угадали!')
else:
    print('Повезет в следующий раз. Это было число,', secret)
